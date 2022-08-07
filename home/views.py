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
    if str(request.user) in ['bhb1s','bhb2s','bhb3s','bhb4s','ghb1s','ghb2s','ghb3s','ghb4s']:
        return redirect('hostelblocksupervisor')
    complains = Complain.objects.all().filter(regno=request.user)
    context = {'complains': complains}
    return render(request, 'home.html', context)


def supervisor(request):
    if str(request.user) != 'supervisor':
        return redirect('/')
    complains = Complain.objects.all()
    context = {'complains': complains}
    return render(request, 'supervisor.html', context)

def hostelBlockSupervisor(request):
    if str(request.user) not in ['bhb1s','bhb2s','bhb3s','bhb4s','ghb1s','ghb2s','ghb3s','ghb4s']:
        return redirect('/')
    if str(request.user) == 'bhb1s':
        filter = 'Boys Hostel Block 1 Supervisor'
    elif str(request.user) == 'bhb2s':
        filter = 'Boys Hostel Block 2 Supervisor'
    elif str(request.user) == 'bhb2s':
        filter = 'Boys Hostel Block 3 Supervisor'
    elif str(request.user) == 'bhb2s':
        filter = 'Boys Hostel Block 4 Supervisor'
    elif str(request.user) == 'ghb1s':
        filter = 'Girls Hostel Block 1 Supervisor'
    elif str(request.user) == 'ghb2s':
        filter = 'Girls Hostel Block 2 Supervisor'
    elif str(request.user) == 'ghb2s':
        filter = 'Girls Hostel Block 3 Supervisor'
    elif str(request.user) == 'ghb2s':
        filter = 'Girls Hostel Block 4 Supervisor'
    complains = Complain.objects.all().filter(hostelBlockSupervisor=filter)
    context = {'complains': complains}
    return render(request, 'hostelblocksupervisor.html', context)

# def hostelBlockDepartmentSupervisor(request):
#     if str(request.user) not in ['bhb1s','bhb2s','bhb3s','bhb4s','ghb1s','ghb2s','ghb3s','ghb4s']:
#         return redirect('/')
#     complains = Complain.objects.all()
#     context = {'complains': complains}
#     return render(request, 'supervisor.html', context)

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
        hostelName = request.POST.get('hostelName')
        hostelBlock = request.POST.get('hostelBlock')
        roomNumber = request.POST.get('hostelRoom')
        date = datetime.now()

        if hostelName == 'Boys Hostel':
            if hostelBlock == 'Block 1':
                hostelBlockSupervisor = 'Boys Hostel Block 1 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 1 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 1 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 1 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 1 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 1 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 1 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected By the Student'

            elif hostelBlock == 'Block 2':
                hostelBlockSupervisor = 'Boys Hostel Block 2 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 2 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 2 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 2 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 2 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 2 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 2 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected By the Student'
            elif hostelBlock == 'Block 3':
                hostelBlockSupervisor = 'Boys Hostel Block 3 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 3 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 3 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 3 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 3 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 3 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 3 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected By the Student'
            elif  hostelBlock == 'Block 4':
                hostelBlockSupervisor = 'Boys Hostel Block 4 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 4 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 4 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 4 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 4 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 4 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Boys Hostel Block 4 Faculty Supervisor'
                else:
                    complainFor = 'Not Selecte3'
            else :
                hostelBlockSupervisor = 'Unknown'
        else :
            if hostelBlock == 'Block 1':
                hostelBlockSupervisor = 'Girls Hostel Block 1 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 1 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 1 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 1 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 1 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 1 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 1 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected By the Student'

            elif hostelBlock == 'Block 2':
                hostelBlockSupervisor = 'Girls Hostel Block 2 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 2 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 2 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 2 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 2 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 2 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 2 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected By the Student'
            elif hostelBlock == 'Block 3':
                hostelBlockSupervisor = 'Girls Hostel Block 3 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 3 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 3 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 3 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 3 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 3 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 3 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected By the Student'
            elif hostelBlock == 'Block 4':
                hostelBlockSupervisor = 'Girls Hostel Block 4 Supervisor'
                if complainFor == 'Mess':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 4 Mess Supervisor'
                elif complainFor == 'Drinking Water':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 4 Drinking Water Supervisor'
                elif complainFor == 'Wifi':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 4 Wifi Supervisor'
                elif complainFor == 'Washrooms':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 4 Washrooms Supervisor'
                elif complainFor == 'Bullying':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 4 Bullying Supervisor'
                elif complainFor == 'Faculty':
                    hostelBlockDepartmentSupervisor = 'Girls Hostel Block 4 Faculty Supervisor'
                else:
                    complainFor = 'Not Selected by the Student'
            else:
                hostelBlockSupervisor = 'Unknown'



        complainDetails = Complain(
            fullname=fullname,
            regno=regno,
            complainFor=complainFor,
            sub=sub,
            desc=desc,
            date=date,
            id="VITBC" + str(date.strftime("%d%m%Y%H%M%S")),
            hostelName = hostelName,
            hostelBlock = hostelBlock,
            roomNumber = roomNumber,
            hostelBlockSupervisor = hostelBlockSupervisor,
            hostelBlockDepartmentSupervisor = hostelBlockDepartmentSupervisor
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


def takeAction(action):
    print("You have to email this person ", action)


def updateComplain(request):
    complain = Complain.objects.get(id=request.POST.get('complainId'))
    if request.method == "POST":
        complain.status = request.POST.get('status')
        complain.action = request.POST.get('action')
        complain.complainResolveDate = request.POST.get('complainResolvedDate')
        print(complain.complainResolveDate)
        # takeAction(complain.action)
        messages.success(request, "Status Successfully updated. And Query "+complain.action+".")
        complain.save()
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
