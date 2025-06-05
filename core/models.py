from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_vehicle_owner = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    driver_license_picture = models.ImageField(upload_to='license_pics/', blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username