from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
# from .models import Department
import os

 
def login_view(request):
     if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
     return render(request, 'login.html')
    
    
def register_view(request):
    
    return render(request, 'register.html')
        
    
    