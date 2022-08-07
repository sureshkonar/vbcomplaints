from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class complainFields(models.Model):
    complainFields = models.CharField(max_length=122)
    def __str__(self):
        return self.complainFields

# Create your models here.
class Complain(models.Model):
    fullname = models.CharField(max_length=122)
    regno = models.CharField(max_length=10)
    complainFor = models.CharField(max_length=122)
    sub = models.CharField(max_length=256)
    desc = models.CharField(max_length=1000)
    date = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=100)

    hostelName = models.CharField(max_length=100)
    hostelBlock = models.CharField(max_length=100)
    roomNumber = models.CharField(max_length=100)

    hostelBlockSupervisor = models.CharField(max_length=100, default='Not Assigned')
    hostelBlockDepartmentSupervisor = models.CharField(max_length=100, default='Not Assigned')
    workerName = models.CharField(max_length=100, default='Not Assigned')

    complainResolveDate = models.DateField(null = True, blank=True)


    status = models.CharField(max_length=10, default='Pending')
    action = models.CharField(max_length=50, default='No Action Taken', choices=[('Forwarded to Electrician','Forwarded to Electrician'),('Forwarded to Hostel Warden','Forwarded to Hostel Warden'),('Forwarded to Cleaning Staff','Forwarded to Cleaning Staff'),('Forwarded to Security','Forwarded to Security')])



    def __str__(self):
        return self.id


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hostelGender = models.CharField(max_length=20, choices=[('Boys Hostel','Boys Hostel'), ('Girls Hostel','Girls Hostel')])
    hostelBlock = models.CharField(max_length=10, choices=[('Block 1','Block 1'),('Block 2','Block 2'),('Block 3','Block 3'),('Block 4','Block 4')])
    roomNo = models.CharField(max_length=5)
    date = models.DateField()

    def __str__(self):
        return self.user.username
