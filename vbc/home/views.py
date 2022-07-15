from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def newc(request):
    return render(request, 'newcomplaint.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')
