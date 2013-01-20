from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your models here.

class GearItem(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    dayRentalPrice = models.PositiveIntegerField()
    user = models.CharField(max_length=50)
    userEmail = models.CharField(max_length=100)
    is_available = models.BooleanField()
    #pic = models.ImageField(upload_to=None)
