from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('SUV', 'SUV'),
        ('SEDAN', 'Sedan'),
        ('TRUCK', 'Truck'),
        ('HATCHBACK', 'Hatchback'),
        ('VAN', 'Van'),
        ('SPORTS', 'Sports Car'),
        ('LUXURY', 'Luxury Vehicle'),
        ('ELECTRIC', 'Electric Vehicle'),
        ('HYBRID', 'Hybrid Vehicle'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_TYPES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='vehicles', null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='vehicle_images/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Rental(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rental #{self.id} - {self.vehicle}"