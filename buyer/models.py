from django.db import models

class Buyer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        # Returning the full name (first name + last name)
        return f'{self.first_name} {self.last_name}'
