from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Signup
from django.contrib import messages
from django.contrib.auth import  logout
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request, 'home.html')


def newc(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request, 'newcomplaint.html')


def profile(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request, 'profile.html')


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatpassword')
        registrationNumber = request.POST.get('registrationno')
        if password == repeatPassword:
            user = Signup(name=email, password=password, date=datetime.today(), registrationNumber=registrationNumber)
            user.save()
            messages.success(request, "You are successfully registered!")
            return redirect('/')
        else:
            messages.warning(request, "Passwords did not match...")
    return render(request, 'signup.html')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('regno')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Invalid Credentials...")

    return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    return redirect('/')
