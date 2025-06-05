from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'vehicle_type', 
                 'daily_rate', 'image', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }