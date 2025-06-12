from django.core.management.base import BaseCommand
from vehicles.models import Vehicle

def run():
    # Map of vehicle names to their correct image files
    image_mapping = {
        'Nissan Patrol': 'vehicle_images/nissan-patrol-2022.jpg',
        'Mercedes GLC': 'vehicle_images/Mercedes_benz_glc.png',
        'Porsche 911': 'vehicle_images/porche.png',
        'Toyota Avanza': 'vehicle_images/avanza.png',
        'Hyundai Stargazer': 'vehicle_images/Stargazer.png',
        'Honda CR-V': 'vehicle_images/Honda_srv.png',
    }

    # Update each vehicle's image
    for vehicle in Vehicle.objects.all():
        vehicle_name = f"{vehicle.make} {vehicle.model}"
        if vehicle_name in image_mapping:
            vehicle.image = image_mapping[vehicle_name]
            vehicle.save()
            print(f"Updated {vehicle_name} with image: {vehicle.image}")
        else:
            print(f"No matching image found for: {vehicle_name}")

if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rentalia.settings')
    django.setup()
    run() 