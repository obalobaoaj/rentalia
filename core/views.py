from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from django import template
from django.contrib.auth.forms import UserCreationForm
from vehicles.models import Vehicle, Rental
from django.db.models import Sum, Q
from django.utils import timezone

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')

@login_required
def dashboard(request):
    # Get user's rental statistics
    user_rentals = Rental.objects.filter(renter=request.user)
    active_rentals = user_rentals.filter(
        start_date__lte=timezone.now().date(),
        end_date__gte=timezone.now().date(),
        is_active=True
    )
    
    # Calculate total spent
    total_spent = user_rentals.aggregate(total=Sum('total_cost'))['total'] or 0
    
    # Get recent rentals
    recent_rentals = user_rentals.order_by('-created_at')[:3]
    
    # Get featured vehicles (available vehicles with lowest daily rate)
    featured_vehicles = Vehicle.objects.filter(is_available=True).order_by('daily_rate')[:4]
    
    # Get available vehicles count
    available_vehicles = Vehicle.objects.filter(is_available=True).count()
    
    context = {
        'user': request.user,
        'total_rentals': user_rentals.count(),
        'active_rentals': active_rentals.count(),
        'available_vehicles': available_vehicles,
        'total_spent': total_spent,
        'recent_rentals': recent_rentals,
        'featured_vehicles': featured_vehicles,
        'today': timezone.now().date(),
    }
    return render(request, 'dashboard.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('landing')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Rentalia, {user.username}!')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/signup.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

@login_required
def profile(request):
    if request.method == 'POST':
        # Update profile information
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        
        # Handle profile picture upload
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
        
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, 'account/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('change_password')
            
        if new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
            return redirect('change_password')
            
        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)  # Keep user logged in
        messages.success(request, 'Password changed successfully!')
        return redirect('profile')
        
    return render(request, 'account/change_password.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        
        if not request.user.check_password(password):
            messages.error(request, 'Password is incorrect.')
            return redirect('delete_account')
            
        if not confirm:
            messages.error(request, 'Please confirm that you understand this action cannot be undone.')
            return redirect('delete_account')
            
        # Check for active rentals
        active_rentals = Rental.objects.filter(
            renter=request.user,
            end_date__gte=timezone.now().date(),
            is_active=True
        ).exists()
        
        if active_rentals:
            messages.error(request, 'You cannot delete your account while you have active rentals.')
            return redirect('delete_account')
            
        # Delete the user
        request.user.delete()
        messages.success(request, 'Your account has been permanently deleted.')
        return redirect('landing')
        
    return render(request, 'account/delete_account.html')