from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Complain
from home.models import Signup
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
import re

# Create your views here.


def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request, 'home.html')


def newc(request):
    if request.user.is_anonymous:
        return redirect('/')
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        regno = request.POST.get('regno')
                                                                                 # Registration number Regular Expression 
        pattern ='[1-2][0,1,9][B,M,PHD][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]'
        x= re.match(pattern, regno)
        if x:
            print('Valid Registration Number')
        else:
            print(request,'Invalid Registration Number')
            return render(request, 'newcomplaint.html')
        sub = request.POST.get('sub')
        desc = request.POST.get('desc')
        complainFor = request.POST.get('dropdown')
        complainDetails = Complain(
            fullname=fullname,
            regno=regno,
            complainFor=complainFor,
            sub=sub,
            desc=desc,
            date=datetime.today()
        )
        complainDetails.save()
        messages.success(request, "Your Complain is successfully Submitted!")

    return render(request, 'newcomplaint.html')


def profile(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request, 'profile.html')


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
                                                                        # Email  Regular Expression 
        address ='\S.*@vitbhopal.ac.in$'
        y= re.match(address, email)
        if y:
            print('Valid mail')
        else:
            print('Invalid Mail , Please Enter "@vitbhopal.ac.in" Domain Mail')
            messages.warning( request,'Invalid Mail , Please Enter "@vitbhopal.ac.in" Domain Mail...')
            return render(request, 'signup.html')

        password = request.POST.get('password')
        repeatPassword = request.POST.get('repeatpassword')
                                                                            # Password Format Regular Expression 
        format = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(format)
        res = re.search(match_re,repeatPassword )
        if res:
            print("Valid Password")
        else:
            print("Invalid Password")
            messages.warning( request,'Password to be between 8 and 18 characters with at least one capital letter, one number and one special character....')
            return render(request, 'signup.html')

        registrationNumber = request.POST.get('registrationno')
                                                                            # Registration number Regular Expression 
        pattern ='[1-2][0,1,9][B,M,PHD][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]'
        x= re.match(pattern, registrationNumber)
        if x:
            print('Valid Registration Number')
        else:
            print('Invalid Registration Number')
            messages.warning( request,"Invalid Registration Number...")
            return render(request, 'signup.html')
        fullname = request.POST.get('name')
        hostelGender = request.POST.get('hostelgender')
        hostelBlock = request.POST.get('hostelBlock')
        roomNo = request.POST.get('roomNumber')
        if password == repeatPassword:
            User.objects.create_user(username=registrationNumber, email=email, password=password)
            userDetails = Signup(
                email=email,
                password=password,
                fullname=fullname,
                regno=registrationNumber,
                hostelGender=hostelGender,
                hostelBlock=hostelBlock,
                roomNo=roomNo,
                date=datetime.today()
            )
            userDetails.save()
            messages.success(request, "You are successfully registered!")
            return redirect('/')
        else:
            messages.warning(request, "Passwords did not match...")
    return render(request, 'signup.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('regno')
                                                                                # Registration number Regular Expression 
        pattern ='[1-2][0,1,9][B,M,PHD][A-Z][A-Z][0-9][0-9][0-9][0-9][0-9]'
        x= re.match(pattern, username)
        if x:
            print('Valid Registration Number')
        else:
            print('Invalid Registration Number')
            messages.warning( request,"Invalid Registration Number...")
            return render(request, 'login.html')


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
