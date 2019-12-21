from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class PerfectHotel(models.Model):
    star = models.IntegerField()
    img = models.ImageField(upload_to='perfecthotel')

class TopDestination(models.Model):
    wifi = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    bathroom = models.BooleanField(default=False)
    content = models.TextField(max_length=100)
    img = models.ImageField(upload_to='topdestination')
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    price = models.IntegerField()

class USP(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    img = models.ImageField(upload_to='usp')

class DiscoverTheWorld(models.Model):
    img = models.ImageField(upload_to='discover')
    flag = models.CharField(max_length=100)
    subname = models.CharField(max_length=100)
    catename = models.CharField(max_length=100)
    numpro = models.IntegerField()

class VisitorExp(models.Model):
    img = models.ImageField(upload_to='visitexp')
    name = models.CharField(max_length=100)
    firm = models.CharField(max_length=100)
    context = models.TextField(max_length=100)
