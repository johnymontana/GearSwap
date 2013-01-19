from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your models here.

class GearItem(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

