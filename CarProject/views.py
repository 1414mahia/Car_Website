# views.py
from django.shortcuts import render, get_object_or_404
from category.models import Category
from car.models import CarProfile

def home(request, category_slug=None):
    categories = Category.objects.all()
    data = CarProfile.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)  # This prevents DoesNotExist errors
        data = CarProfile.objects.filter(category=category)

    return render(request, 'home.html', {'data': data, 'categories': categories})
