from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone =  models.CharField(max_length=13)

    ROLE_CHOICES = (
        ('USER','User'),
        ('DOCTOR' ,'Doctor'),
        ('ADMIN','Admin'),
    )

    role = models.CharField(max_length=10 , choices= ROLE_CHOICES, default='USER')