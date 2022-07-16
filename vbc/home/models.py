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
        return self.regno + " " + self.complainFor + " " + str(self.date)

class Signup(models.Model):
    fullname = models.CharField(max_length=122)
    regno = models.CharField(max_length=10)

    date = models.DateField()

    def __str__(self):
        return self.regno + " " + self.complainFor + " " + str(self.date)


