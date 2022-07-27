from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Complain(models.Model):
    fullname = models.CharField(max_length=122)
    regno = models.CharField(max_length=10)
    complainFor = models.CharField(max_length=122)
    sub = models.CharField(max_length=256)
    desc = models.CharField(max_length=1000)
    date = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=100)
    roomDetails = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='Pending')
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
