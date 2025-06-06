from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum, Count
from django.utils import timezone
from .models import Vehicle, Location, Rental, Earnings

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_info', 'display_image', 'vehicle_type', 'daily_rate', 
                   'location', 'is_available', 'owner')
    list_filter = ('vehicle_type', 'is_available', 'location', 'year')
    search_fields = ('make', 'model', 'owner__username', 'location__name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Vehicle Information', {
            'fields': ('make', 'model', 'year', 'vehicle_type', 'description')
        }),
        ('Rental Details', {
            'fields': ('daily_rate', 'is_available', 'location')
        }),
        ('Ownership', {
            'fields': ('owner', 'image')
        }),
    )
    
    def vehicle_info(self, obj):
        return f"{obj.year} {obj.make} {obj.model}"
    vehicle_info.short_description = 'Vehicle'
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', 
                             obj.image.url)
        return "No image"
    display_image.short_description = 'Image'
    
    actions = ['mark_available', 'mark_unavailable']
    
    def mark_available(self, request, queryset):
        queryset.update(is_available=True)
    mark_available.short_description = "Mark selected vehicles as available"
    
    def mark_unavailable(self, request, queryset):
        queryset.update(is_available=False)
    mark_unavailable.short_description = "Mark selected vehicles as unavailable"

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_count')
    search_fields = ('name',)
    
    def vehicle_count(self, obj):
        return obj.vehicles.count()
    vehicle_count.short_description = 'Number of Vehicles'

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehicle', 'renter', 'start_date', 'end_date', 
                   'total_cost', 'is_active', 'rental_status')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('vehicle__make', 'vehicle__model', 'renter__username')
    ordering = ('-created_at',)
    date_hierarchy = 'start_date'
    
    def rental_status(self, obj):
        today = timezone.now().date()
        
        if not obj.is_active:
            status_html = '<span style="color: red;">Cancelled</span>'
        elif obj.end_date < today:
            status_html = '<span style="color: gray;">Completed</span>'
        elif obj.start_date <= today <= obj.end_date:
            status_html = '<span style="color: green;">Active</span>'
        else:
            status_html = '<span style="color: blue;">Upcoming</span>'
        
        return format_html(status_html)
    rental_status.short_description = 'Status'

@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):
    list_display = ('rental', 'owner_name', 'vehicle_info', 'owner_earnings', 
                   'platform_commission', 'payment_status', 'paid_at')
    list_filter = ('payment_status', 'created_at', 'paid_at')
    search_fields = ('rental__vehicle__make', 'rental__vehicle__model', 
                    'rental__vehicle__owner__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    
    actions = ['mark_as_paid', 'mark_as_pending']
    
    def owner_name(self, obj):
        return obj.rental.vehicle.owner.username
    owner_name.short_description = 'Owner'
    
    def vehicle_info(self, obj):
        return f"{obj.rental.vehicle.year} {obj.rental.vehicle.make} {obj.rental.vehicle.model}"
    vehicle_info.short_description = 'Vehicle'
    
    def mark_as_paid(self, request, queryset):
        queryset.update(payment_status='PAID', paid_at=timezone.now())
    mark_as_paid.short_description = "Mark selected earnings as paid"
    
    def mark_as_pending(self, request, queryset):
        queryset.update(payment_status='PENDING', paid_at=None)
    mark_as_pending.short_description = "Mark selected earnings as pending"
    
    def changelist_view(self, request, extra_context=None):
        # Calculate summary statistics
        response = super().changelist_view(request, extra_context)
        
        try:
            queryset = self.get_queryset(request)
            total_earnings = queryset.aggregate(
                total_owner_earnings=Sum('owner_earnings'),
                total_platform_commission=Sum('platform_commission'),
                total_transactions=Count('id'),
                pending_payments=Sum('owner_earnings', 
                                   filter={'payment_status': 'PENDING'})
            )
            
            # Add summary to the response
            if not response.context_data:
                response.context_data = {}
            
            response.context_data['summary_stats'] = {
                'total_owner_earnings': total_earnings['total_owner_earnings'] or 0,
                'total_platform_commission': total_earnings['total_platform_commission'] or 0,
                'total_transactions': total_earnings['total_transactions'] or 0,
                'pending_payments': total_earnings['pending_payments'] or 0
            }
            
        except (AttributeError, KeyError):
            pass
        
        return response
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ('rental', 'owner_earnings', 'platform_commission', 'created_at')
        return ('created_at',)

    class Media:
        css = {
            'all': ('admin/css/earnings.css',)
        }