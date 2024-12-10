from django.db import models
from brand.models import Brand
from category.models import Category
from django.contrib.auth.models import User

class CarProfile(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)  # Linking many categories to one car profile
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)  # Linking to the Brand model
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking to the User (buyer)
    image=models.ImageField(upload_to='uplode/',blank=True,null=True)

    def __str__(self):
        return self.name