from django import forms
from .models import CarProfile

class CarForm(forms.ModelForm):
    class Meta:
        model = CarProfile
        fields = '__all__'  # Corrected the typo here
