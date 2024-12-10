"""
URL configuration for CarProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views  # Import views for the home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name ='home_page'),
    path('category/<slug:category_slug>/',views.home,name ='category_wise_post'),
    path('buyer/', include('buyer.urls')),  
    path('car/', include('car.urls')),  
    path('brand/', include('brand.urls')),  
    path('category/', include('category.urls')), 
]

# Serving media files in development mode

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)