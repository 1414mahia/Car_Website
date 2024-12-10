from typing import Any
from django.shortcuts import render,redirect

from car.models import CarProfile


from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login,update_session_auth_hash,logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.
#def add_author(request):
   # if request.method =='POST':
        
      #author_form =forms.AuthorForm(request.POST) # form class er AuthorFrom
     # if author_form.is_valid():
         #  author_form.save()
          # return redirect("add_author")
   # else:
       # author_form =forms.AuthorForm() # user website a dhukche but kono data pass kore nai
    #return render(request,'add_author.html',{'form':author_form})
    
def register(request):
   if request.method =='POST':
        
      registration_form =forms.RegistrationForm(request.POST) # form class er AuthorFrom
      if registration_form.is_valid():
         registration_form.save()
         messages.success(request,"Account created successfully")
         return redirect("register")
      
   else:
      registration_form =forms.RegistrationForm() # user website a dhukche but kono data pass kore nai
   return render(request,'register.html',{'form':registration_form,'type':'register'})




class UserLoginView(LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy("profile")
    def form_valid(self, form):
        messages.success(self.request,'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    
    



@login_required
def profile(request):
    data =CarProfile.objects.filter(buyer =request.user) #specific person er data er jonno
    
    return render(request,'buyer_profile.html',{'data':data})



def user_logout(request):
    logout(request)
    return redirect("login")