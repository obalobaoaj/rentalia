from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('rent/<int:vehicle_id>/', views.rent_vehicle, name='rent_vehicle'),
    path('update/<int:vehicle_id>/', views.update_vehicle, name='update_vehicle'),
    path('delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
    path('rental/cancel/<int:rental_id>/', views.cancel_rental, name='cancel_rental'),
]