from django.db import models

class Etud(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    password1 = models.CharField(max_length=10)
    matruculation_etud = models.CharField(max_length=100,null=True,blank=True)
    USERNAME_FIELD = 'username'
    image = models.ImageField(upload_to=None,height_field=None,width_field=None)
    # Add any other fields you want to save for your Etud model

class Manager(models.Model):
    username = models.CharField(max_length=100)
    id = models.IntegerField(max_length=10 , primary_key= True)
    password = models.CharField(max_length=15)