from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User

@admin.register(User)
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
