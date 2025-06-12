from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('profile/', views.profile, name='profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/delete/', views.delete_account, name='delete_account'),
    
    # Management URLs
    path('management/', views.management_dashboard, name='management_dashboard'),
    path('management/add-vehicle/', views.admin_add_vehicle, name='management_add_vehicle'),
    path('management/rental-requests/', views.rental_requests, name='rental_requests'),
    path('management/users/', views.manage_users, name='manage_users'),
    path('management/users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('management/users/<int:user_id>/activate/', views.activate_user, name='activate_user'),
    path('management/users/<int:user_id>/deactivate/', views.deactivate_user, name='deactivate_user'),
    path('management/reports/', views.reports, name='reports'),
    path('management/transactions/', views.all_transactions, name='all_transactions'),
    path('management/rental/<int:rental_id>/approve/', views.approve_rental, name='approve_rental'),
    path('management/rental/<int:rental_id>/reject/', views.reject_rental, name='reject_rental'),
]