from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class College(models.Model):
    name    =   models.CharField(max_length=250)
    dob     =   models.DateField()
    age     =   models.IntegerField()
    gender  =   models.CharField(max_length=250)
    phone   =   models.TextField()
    mail_id =   models.EmailField()
    dept    =   models.CharField(max_length=250)
    course  =   models.CharField(max_length=250)

    def __str__(self):
        return self.name









