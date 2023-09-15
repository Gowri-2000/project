from django.db import models

# Create your models here.
class logindata(models.Model):
    username=models.CharField(max_length=20,default="")
    password=models.CharField(max_length=20,default="")
