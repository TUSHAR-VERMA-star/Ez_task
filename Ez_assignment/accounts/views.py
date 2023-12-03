from django.shortcuts import render, redirect
from .models import *

from django.contrib import messages, auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def RegisterView(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            value = User.objects.get(email=email)
            
            return redirect('sign-up')
        except ObjectDoesNotExist:
            pass
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        
        return redirect('sign-in')

    return render(request, "accounts/sign-up.html")


def LoginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        auth.login(request, user)
        return redirect('home')
    return render(request, "accounts/sign-in.html")


def LogoutView(request):
    auth.logout(request)
    return redirect('sign-up') 