from django.db import models


# Create your models here.
class Signup(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=16)
    date = models.DateField()
    registrationNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.registrationNumber


