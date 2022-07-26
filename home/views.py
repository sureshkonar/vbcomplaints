from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from datetime import datetime, date
from home.models import Complain
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    if str(request.user) == 'supervisor':
        return redirect('supervisor')
    complains = Complain.objects.all().filter(regno=request.user)
    context = {'complains': complains}
    return render(request, 'home.html', context)


def supervisor(request):
    if str(request.user) != 'supervisor':
        return redirect('/')
    complains = Complain.objects.all()
    context = {'complains': complains}
    return render(request, 'supervisor.html', context)


def newc(request):
    if request.user.is_anonymous:
        return redirect('/')
    users = User.objects.all().filter(username=request.user)
    context = {'users': users}
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        regno = request.POST.get('regno')
        sub = request.POST.get('sub')
        desc = request.POST.get('desc')
        complainFor = request.POST.get('dropdown')
        date = datetime.now()
        complainDetails = Complain(
            fullname=fullname,
            regno=regno,
            complainFor=complainFor,
            sub=sub,
            desc=desc,
            date=date,
            id = "VITBC" + regno + str(date.strftime("%d%m%Y%H%M%S"))
        )
        complainDetails.save()
        messages.success(request, "Your Complain is successfully Submitted!")

    return render(request, 'newcomplaint.html', context)


def profile(request):
    if request.user.is_anonymous:
        return redirect('/')
    users = User.objects.all().filter(username=request.user)
    context = {'users': users}

    return render(request, 'profile.html', context)


def updateComplain(request):
    complain = Complain.objects.get(id = request.POST.get('complainId'))
    if request.method == "POST":
        complain.status = request.POST.get('status')
        complain.save()
        messages.success(request, "Status Successfully updated.")
        return redirect('supervisor')
    return render(request, 'supervisor.html')


def signup(request):
    if request.method == "POST":
        oldpassword = request.POST.get('oldpassword')
        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatpassword')
        registrationNumber = request.POST.get('registrationno')

        user = authenticate(username=registrationNumber, password=oldpassword)
        if user is not None:
            if password == repeatPassword:
                user.set_password(str(password))
                user.save()
                messages.success(request, "You have successfully changed your password!")
                return redirect('/')
            else:
                messages.warning(request, "Passwords did not match...")

            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials...")

    return render(request, 'signup.html')


def loginUser(request):
    if request.method == "POST":
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
