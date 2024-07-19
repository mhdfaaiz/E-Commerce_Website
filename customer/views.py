from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer
# Create your views here.
def account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            
            #creates user accounts
            user=User.objects.create(
                username=username,
                password=password,
                email=email
            )
            #creates customer account
            customer=Customer.objects.create(
                user=user,
                phone=phone,
            )
            return redirect('home')
        except Exception as e:
            error_message="Duplicate username or invalid credentials"
    return render(request,'account.html')