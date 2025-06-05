from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vehicle, Rental, Location
from .forms import VehicleForm
from datetime import datetime
from django.utils import timezone


@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.filter(is_available=True)

    location_id = request.GET.get('location')
    selected_location = None
    if location_id:
        try:
            selected_location = Location.objects.get(id=location_id)
            vehicles = vehicles.filter(location=selected_location)
        except Location.DoesNotExist:
            selected_location = None
    locations = Location.objects.all()
    context = {
        'vehicles': vehicles,
        'suvs': vehicles.filter(vehicle_type='SUV'),
        'sedans': vehicles.filter(vehicle_type='SEDAN'),
        'trucks': vehicles.filter(vehicle_type='TRUCK'),
        'Hybrids': vehicles.filter(vehicle_type='HYBRID'),
        'electric': vehicles.filter(vehicle_type='ELECTRIC'),
        'selected_location': selected_location,
        'locations': locations,
    }
    return render(request, 'vehicles/list.html', context)


@login_required
def add_vehicle(request):
    if not request.user.is_staff:  # Only allow staff/admin users
        messages.error(request, 'You are not authorized to add vehicles.')
        return redirect('vehicle_list')
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            messages.success(request, 'Vehicle added successfully!')
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/add.html', {'form': form})


@login_required
def rent_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id, is_available=True)
    locations = Location.objects.all()
    
    if request.method == 'POST':
        location_id = request.POST.get('location')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        try:
            location = Location.objects.get(id=location_id)
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            
            if start_date < timezone.now().date():
                messages.error(request, 'Start date cannot be in the past.')
                return redirect('rent_vehicle', vehicle_id=vehicle_id)
                
            if end_date <= start_date:
                messages.error(request, 'End date must be after start date.')
                return redirect('rent_vehicle', vehicle_id=vehicle_id)
            
            # Calculate total days and cost
            days = (end_date - start_date).days
            total_cost = vehicle.daily_rate * days
            
            # Create the rental
            rental = Rental.objects.create(
                vehicle=vehicle,
                renter=request.user,
                start_date=start_date,
                end_date=end_date,
                total_cost=total_cost
            )
            
            # Update vehicle availability
            vehicle.is_available = False
            vehicle.location = location
            vehicle.save()
            
            messages.success(request, 'Vehicle rented successfully!')
            return redirect('dashboard')
            
        except (ValueError, Location.DoesNotExist):
            messages.error(request, 'Invalid form data. Please check your inputs.')
            return redirect('rent_vehicle', vehicle_id=vehicle_id)
    
    context = {
        'vehicle': vehicle,
        'locations': locations,
        'today': timezone.now().date(),
    }
    return render(request, 'vehicles/rent_form.html', context)


@login_required
def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    # Check if user is the owner
    if not request.user.is_vehicle_owner or vehicle.owner != request.user:
        messages.error(request, 'You are not authorized to edit this vehicle.')
        return redirect('vehicle_list')
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle updated successfully!')
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    
    return render(request, 'vehicles/update.html', {'form': form, 'vehicle': vehicle})


@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    # Check if user is the owner
    if not request.user.is_vehicle_owner or vehicle.owner != request.user:
        messages.error(request, 'You are not authorized to delete this vehicle.')
        return redirect('vehicle_list')
    
    # Check if vehicle has active rentals
    active_rentals = Rental.objects.filter(
        vehicle=vehicle,
        end_date__gte=timezone.now().date(),
        is_active=True
    ).exists()
    
    if active_rentals:
        messages.error(request, 'Cannot delete vehicle with active rentals.')
        return redirect('vehicle_list')
    
    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, 'Vehicle deleted successfully!')
        return redirect('vehicle_list')
    
    return render(request, 'vehicles/delete.html', {'vehicle': vehicle})


@login_required
def cancel_rental(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    
    # Check if user is the renter
    if rental.renter != request.user:
        messages.error(request, 'You are not authorized to cancel this rental.')
        return redirect('dashboard')
    
    # Check if rental is still active and hasn't started
    if not rental.is_active or rental.start_date <= timezone.now().date():
        messages.error(request, 'Cannot cancel an ongoing or completed rental.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        # Update rental status
        rental.is_active = False
        rental.save()
        
        # Make vehicle available again
        rental.vehicle.is_available = True
        rental.vehicle.save()
        
        messages.success(request, 'Rental cancelled successfully!')
        return redirect('dashboard')
    
    return render(request, 'vehicles/cancel_rental.html', {'rental': rental})