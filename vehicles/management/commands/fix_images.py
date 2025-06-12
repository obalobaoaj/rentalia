from django.core.management.base import BaseCommand
from vehicles.models import Vehicle

class Command(BaseCommand):
    help = 'Fix vehicle image paths'

    def handle(self, *args, **options):
        # Map of vehicle names to their correct image files
        image_mapping = {
            'Toyota Camry': 'vehicle_images/avanza.png',  # Using Avanza image for Camry
            'Honda CR-V': 'vehicle_images/Honda_srv.png',
            'Tesla Model 3': 'vehicle_images/porche.png',  # Using Porsche image for Tesla
        }

        # Update each vehicle's image
        for vehicle in Vehicle.objects.all():
            vehicle_name = f"{vehicle.make} {vehicle.model}"
            if vehicle_name in image_mapping:
                vehicle.image = image_mapping[vehicle_name]
                vehicle.save()
                self.stdout.write(self.style.SUCCESS(f"Updated {vehicle_name} with image: {vehicle.image}"))
            else:
                self.stdout.write(self.style.WARNING(f"No matching image found for: {vehicle_name}")) 