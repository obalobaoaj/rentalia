from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.db.models import Sum, Count, Q
from django.utils import timezone
from .models import User
from vehicles.models import Vehicle, Rental, Earnings, Location

class CustomAdminSite(admin.AdminSite):
    site_header = 'Rentalia Administration'
    site_title = 'Rentalia Admin Portal'
    index_title = 'Welcome to Rentalia Administration'

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        
        # Get statistics
        extra_context['total_vehicles'] = Vehicle.objects.count()
        
        # Active rentals (not cancelled and currently ongoing)
        extra_context['active_rentals'] = Rental.objects.filter(
            is_active=True,
            start_date__lte=timezone.now().date(),
            end_date__gte=timezone.now().date()
        ).count()
        
        extra_context['total_users'] = User.objects.count()
        
        # Calculate total earnings excluding cancelled rentals
        earnings_data = Earnings.objects.exclude(payment_status='CANCELLED').aggregate(
            total_earnings=Sum('owner_earnings'),
            total_commission=Sum('platform_commission')
        )
        
        # Calculate cancelled earnings
        cancelled_earnings = Earnings.objects.filter(payment_status='CANCELLED').aggregate(
            cancelled_amount=Sum('owner_earnings')
        )['cancelled_amount'] or 0
        
        extra_context['total_earnings'] = earnings_data['total_earnings'] or 0
        extra_context['total_commission'] = earnings_data['total_commission'] or 0
        extra_context['cancelled_earnings'] = cancelled_earnings
        
        return super().index(request, extra_context)

# Create an instance of the custom admin site
admin_site = CustomAdminSite()

# Register models with the custom admin site
@admin.register(User, site=admin_site)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_vehicle_owner', 
                   'is_staff', 'is_active', 'display_profile_picture')
    list_filter = ('is_vehicle_owner', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 
                                    'address', 'age', 'date_of_birth')}),
        ('Profile', {'fields': ('profile_picture', 'driver_license_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 
                                  'is_vehicle_owner', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_vehicle_owner'),
        }),
    )
    
    def display_profile_picture(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', 
                             obj.profile_picture.url)
        return "No picture"
    display_profile_picture.short_description = 'Profile Picture'

    actions = ['make_vehicle_owner', 'remove_vehicle_owner']

    def make_vehicle_owner(self, request, queryset):
        queryset.update(is_vehicle_owner=True)
    make_vehicle_owner.short_description = "Mark selected users as vehicle owners"

    def remove_vehicle_owner(self, request, queryset):
        queryset.update(is_vehicle_owner=False)
    remove_vehicle_owner.short_description = "Remove vehicle owner status"

# Import and register the models from vehicles/admin.py
from vehicles.admin import VehicleAdmin, LocationAdmin, RentalAdmin, EarningsAdmin

admin_site.register(Vehicle, VehicleAdmin)
admin_site.register(Location, LocationAdmin)
admin_site.register(Rental, RentalAdmin)
admin_site.register(Earnings, EarningsAdmin)

# Replace the default admin site
admin.site = admin_site
