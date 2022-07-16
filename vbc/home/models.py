from django.db import models


# Create your models here.
class Complain(models.Model):
    fullname = models.CharField(max_length=122)
    regno = models.CharField(max_length=10)
    complainFor = models.CharField(max_length=122)
    sub = models.CharField(max_length=256)
    desc = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return "VITB" + self.regno + str(self.date) + self.complainFor


class Signup(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=16)
    fullname = models.CharField(max_length=122)
    regno = models.CharField(max_length=10)
    hostelGender = models.CharField(max_length=20)
    hostelBlock = models.CharField(max_length=10)
    roomNo = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.regno
