from django.db import models

class Brand(models.Model):
    # Define choices for the brand
    BRAND_CHOICES = [
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Ferrari', 'Ferrari'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Porsche', 'Porsche'),
        ('Lamborghini', 'Lamborghini'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Land Rover', 'Land Rover'),
    ]

    brand_name = models.CharField(
        max_length=100,
        choices=BRAND_CHOICES,
    )

    def __str__(self):
        return self.brand_name
