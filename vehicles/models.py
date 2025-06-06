from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from decimal import Decimal

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
    
    def total_earnings(self):
        return sum(rental.total_cost for rental in self.rental_set.filter(is_active=True))

class Rental(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    commission_rate = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('10.00'))  # Platform commission in percentage

    def __str__(self):
        return f"Rental #{self.id} - {self.vehicle}"
    
    def calculate_earnings(self):
        if self.is_active:
            platform_commission = (self.total_cost * self.commission_rate) / Decimal('100.00')
            owner_earnings = self.total_cost - platform_commission
            return owner_earnings, platform_commission
        return Decimal('0.00'), Decimal('0.00')

class Earnings(models.Model):
    rental = models.OneToOneField(Rental, on_delete=models.CASCADE)
    owner_earnings = models.DecimalField(max_digits=10, decimal_places=2)
    platform_commission = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('CANCELLED', 'Cancelled')
    ], default='PENDING')
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Earnings"

    def __str__(self):
        return f"Earnings for {self.rental}"

    def mark_as_paid(self):
        self.payment_status = 'PAID'
        self.paid_at = timezone.now()
        self.save()

@receiver(post_save, sender=Rental)
def create_or_update_earnings(sender, instance, created, **kwargs):
    if created or instance.is_active:
        owner_earnings, platform_commission = instance.calculate_earnings()
        Earnings.objects.update_or_create(
            rental=instance,
            defaults={
                'owner_earnings': owner_earnings,
                'platform_commission': platform_commission,
                'payment_status': 'PENDING' if instance.is_active else 'CANCELLED'
            }
        )