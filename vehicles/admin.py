from django.contrib import admin
from .models import Vehicle
from .models import Location

admin.site.register(Vehicle)
admin.site.register(Location)