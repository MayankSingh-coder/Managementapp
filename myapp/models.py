from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Admin_user(models.Model):
    phone = models.CharField(max_length=13, blank=True)
    fullname = models.CharField(max_length=200,default = "fullname")
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.fullname


class Refrence_user(models.Model):
    fullname = models.CharField(max_length=200,default = "fullname")
    phone = models.CharField(max_length=13, blank=True)
    email = models.EmailField(max_length=254)
    designation=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.fullname