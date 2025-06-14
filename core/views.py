from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from django import template
from django.contrib.auth.forms import UserCreationForm
from vehicles.models import Vehicle, Rental
from django.db.models import Sum, Q, Count, Avg
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import datetime, timedelta
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.db.models import F, ExpressionWrapper, DurationField

User = get_user_model()

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

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    # Get total earnings
    total_earnings = Rental.objects.aggregate(total=Sum('total_cost'))['total'] or 0

    # Get counts
    active_rentals = Rental.objects.filter(is_active=True).count()
    available_vehicles = Vehicle.objects.filter(is_available=True).count()
    total_users = User.objects.count()
    cancelled_rentals = Rental.objects.filter(is_active=False).count()

    # Get recent transactions
    recent_transactions = Rental.objects.all().order_by('-created_at')[:5]

    context = {
        'total_earnings': total_earnings,
        'active_rentals': active_rentals,
        'available_vehicles': available_vehicles,
        'total_users': total_users,
        'cancelled_rentals': cancelled_rentals,
        'recent_transactions': recent_transactions,
    }

    return render(request, 'management/dashboard.html', context)

@user_passes_test(is_admin)
def admin_add_vehicle(request):
    if request.method == 'POST':
        try:
            # Get the current user as the owner
            vehicle = Vehicle.objects.create(
                owner=request.user,
                make=request.POST['make'],
                model=request.POST['model'],
                year=request.POST['year'],
                vehicle_type=request.POST['vehicle_type'],
                description=request.POST['description'],
                image=request.FILES['image'],
                daily_rate=request.POST['daily_rate'],
                is_available=True
            )
            messages.success(request, f'Vehicle "{vehicle.make} {vehicle.model}" has been added successfully!')
            return redirect('management_dashboard')
        except Exception as e:
            messages.error(request, f'Error adding vehicle: {str(e)}')
            return redirect('management_add_vehicle')
    
    return render(request, 'management/add_vehicle.html')

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('management_dashboard')
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
                if user.is_staff:
                    return redirect('management_dashboard')
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

@login_required
def management_dashboard(request):
    # Basic stats
    total_earnings = Rental.objects.aggregate(Sum('total_cost'))['total_cost__sum'] or 0
    active_rentals = Rental.objects.filter(is_active=True).count()
    available_vehicles = Vehicle.objects.filter(is_available=True).count()
    total_users = User.objects.count()
    total_vehicles = Vehicle.objects.count()

    # Weekly revenue data
    today = timezone.now()
    week_ago = today - timedelta(days=7)
    daily_revenue = (
        Rental.objects
        .filter(created_at__gte=week_ago)
        .values('created_at__date')
        .annotate(daily_sum=Sum('total_cost'))
        .order_by('created_at__date')
    )
    weekly_revenue = [0] * 7  # Initialize with zeros
    for revenue in daily_revenue:
        day_index = (revenue['created_at__date'].weekday() + 1) % 7
        weekly_revenue[day_index] = float(revenue['daily_sum'])

    # Upcoming reservations
    upcoming_reservations = (
        Rental.objects
        .filter(start_date__gte=today)
        .select_related('vehicle', 'renter')
        .order_by('start_date')[:5]
    )

    # Popular vehicles
    popular_vehicles = (
        Vehicle.objects
        .annotate(rental_count=Count('rental'))
        .order_by('-rental_count')[:5]
    )

    # Recent activities
    recent_activities = []
    
    # Get recent rentals
    recent_rentals = Rental.objects.select_related('vehicle', 'renter').order_by('-created_at')[:10]
    for rental in recent_rentals:
        vehicle_str = f"{rental.vehicle.year} {rental.vehicle.make} {rental.vehicle.model}"
        if rental.is_active:
            activity_type = 'rental'
            description = f"{rental.renter.username} rented {vehicle_str}"
        else:
            activity_type = 'return'
            description = f"{rental.renter.username} returned {vehicle_str}"
        
        recent_activities.append({
            'type': activity_type,
            'description': description,
            'timestamp': rental.created_at
        })

    # Recent transactions
    recent_transactions = Rental.objects.select_related('vehicle', 'renter').order_by('-created_at')[:5]

    context = {
        'total_earnings': total_earnings,
        'active_rentals': active_rentals,
        'available_vehicles': available_vehicles,
        'total_users': total_users,
        'total_vehicles': total_vehicles,
        'weekly_revenue': weekly_revenue,
        'upcoming_reservations': upcoming_reservations,
        'popular_vehicles': popular_vehicles,
        'recent_activities': recent_activities,
        'recent_transactions': recent_transactions,
    }

    return render(request, 'management/dashboard.html', context)

@login_required
def rental_requests(request):
    # Get pending rental requests (newly created rentals that are active)
    pending_rentals = (
        Rental.objects
        .filter(is_active=True)
        .select_related('vehicle', 'renter')
        .order_by('-created_at')
    )
    
    context = {
        'pending_rentals': pending_rentals,
    }
    return render(request, 'management/rental_requests.html', context)

@login_required
def manage_users(request):
    # Get all users except superusers with pagination
    user_list = User.objects.filter(is_superuser=False).order_by('-date_joined')
    paginator = Paginator(user_list, 10)  # Show 10 users per page
    
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    context = {
        'users': users,
    }
    return render(request, 'management/manage_users.html', context)

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        # Update user information
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        
        messages.success(request, f'User {user.username} has been updated successfully.')
        return redirect('manage_users')
    
    return JsonResponse({
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })

@login_required
def activate_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.is_active = True
        user.save()
        messages.success(request, f'User {user.username} has been activated.')
    return redirect('manage_users')

@login_required
def deactivate_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user.is_active = False
        user.save()
        messages.success(request, f'User {user.username} has been deactivated.')
    return redirect('manage_users')

@login_required
def reports(request):
    # Get the selected time period (default to 7 days)
    period = int(request.GET.get('period', 7))
    end_date = timezone.now()
    start_date = end_date - timedelta(days=period)
    previous_start_date = start_date - timedelta(days=period)

    # Calculate current period stats with debug logging
    print(f"Calculating revenue from {start_date} to {end_date}")
    current_rentals = Rental.objects.filter(
        created_at__range=(start_date, end_date),
        is_active=True  # Only count active rentals
    )
    current_revenue = current_rentals.aggregate(Sum('total_cost'))['total_cost__sum'] or 0
    print(f"Current revenue: {current_revenue}")

    # Calculate previous period stats
    previous_rentals = Rental.objects.filter(
        created_at__range=(previous_start_date, start_date),
        is_active=True  # Only count active rentals
    )
    previous_revenue = previous_rentals.aggregate(Sum('total_cost'))['total_cost__sum'] or 0
    print(f"Previous revenue: {previous_revenue}")

    # Calculate revenue growth
    revenue_growth = 0
    if previous_revenue > 0:
        revenue_growth = ((current_revenue - previous_revenue) / previous_revenue) * 100

    # Calculate average rental duration using ExpressionWrapper and F objects
    current_rentals = current_rentals.annotate(
        duration=ExpressionWrapper(
            F('end_date') - F('start_date'),
            output_field=DurationField()
        )
    )
    
    avg_duration = current_rentals.aggregate(
        avg_duration=Avg('duration')
    )['avg_duration']
    
    # Convert duration to days
    if avg_duration:
        avg_rental_duration = avg_duration.days
    else:
        avg_rental_duration = 0

    # Get popular vehicles with their stats
    popular_vehicles = (
        Vehicle.objects
        .annotate(
            rental_count=Count('rental', filter=Q(rental__created_at__range=(start_date, end_date))),
            total_revenue=Sum('rental__total_cost', filter=Q(rental__created_at__range=(start_date, end_date)))
        )
        .filter(rental_count__gt=0)
        .order_by('-rental_count')[:5]
    )

    # Prepare data for revenue trend chart with daily granularity
    labels = []
    revenue_data = []
    
    for i in range(period):
        current_date = end_date.date() - timedelta(days=i)
        daily_revenue = Rental.objects.filter(
            created_at__date=current_date,
            is_active=True
        ).aggregate(
            total=Sum('total_cost')
        )['total'] or 0
        
        labels.insert(0, current_date.strftime('%b %d'))
        revenue_data.insert(0, float(daily_revenue))
        print(f"Revenue for {current_date}: {daily_revenue}")

    # Prepare data for popular vehicles chart
    vehicle_labels = [str(v) for v in popular_vehicles]
    vehicle_data = [v.rental_count for v in popular_vehicles]

    # Get recent rentals with duration annotation
    recent_rentals = (
        Rental.objects
        .select_related('vehicle', 'renter')
        .annotate(
            duration=ExpressionWrapper(
                F('end_date') - F('start_date'),
                output_field=DurationField()
            )
        )
        .order_by('-created_at')[:10]
    )

    monthly_stats = {
        'total_revenue': current_revenue,
        'total_rentals': current_rentals.count(),
        'new_users': User.objects.filter(date_joined__range=(start_date, end_date)).count(),
        'popular_vehicles': popular_vehicles,
    }

    context = {
        'monthly_stats': monthly_stats,
        'revenue_growth': round(revenue_growth, 1),
        'avg_rental_duration': avg_rental_duration,
        'revenue_labels': json.dumps(labels),
        'revenue_data': json.dumps(revenue_data),  # Ensure proper JSON serialization
        'vehicle_labels': json.dumps(vehicle_labels),
        'vehicle_data': vehicle_data,
        'recent_rentals': recent_rentals,
        'selected_period': period,
    }

    return render(request, 'management/reports.html', context)

@login_required
def all_transactions(request):
    # Get all transactions with related data
    transactions = Rental.objects.select_related('vehicle', 'renter').order_by('-created_at')
    
    context = {
        'transactions': transactions,
    }
    return render(request, 'management/transactions.html', context)

@login_required
def approve_rental(request, rental_id):
    if request.method == 'POST':
        rental = get_object_or_404(Rental, id=rental_id)
        rental.is_active = True
        rental.save()
        messages.success(request, 'Rental request approved successfully.')
        return redirect('rental_requests')
    return redirect('rental_requests')

@login_required
def reject_rental(request, rental_id):
    if request.method == 'POST':
        rental = get_object_or_404(Rental, id=rental_id)
        rental.is_active = False
        rental.save()
        messages.success(request, 'Rental request rejected successfully.')
        return redirect('rental_requests')
    return redirect('rental_requests')