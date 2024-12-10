from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    # Define choices for the category
    CATEGORY_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV (Sport Utility Vehicle)'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Sports Car', 'Sports Car'),
        ('EV', 'Electric Vehicle (EV)'),
    ]

    category_name = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        null=True
    )
    slug =models.SlugField(max_length= 100,null=True,blank=True) # pore filed add korar jonno null=true
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.category_name
