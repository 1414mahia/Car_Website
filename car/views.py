from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

from django.urls import reverse_lazy

from car.models import CarProfile


from  car.forms import CarForm

from django.utils.decorators import method_decorator # class er jonno
from django.contrib.auth.decorators import login_required # function er jonno
from django.contrib.auth.views import LoginView,LogoutView


 
#@method_decorator(login_required,name='dispatch') #dispatch hocche unloged user access korte parbe nh
class AddCarPost(CreateView):
    model = CarProfile
    form_class =  CarForm
    template_name = 'buy_car.html'
    success_url = reverse_lazy("profile")  # Correct URL for success
    
    



#@method_decorator(login_required,name='dispatch') 
class EditPostView(UpdateView):
    model =CarProfile
    form_class =CarForm
    template_name='buy_car.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profile")

     
#class base

#@method_decorator(login_required,name='dispatch') 
class DeletePostView(DeleteView):
    model =CarProfile
    
    template_name='delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("profile")
   

#@method_decorator(login_required,name='dispatch') 
class detailView(DeleteView):
    model =CarProfile

    template_name='profile.html'
    pk_url_kwarg = 'id'
     
     
    