from django.db import models

# Create your models here.
class datainsert(models.Model):
    name = models.CharField(max_length=200,default="x")
    play = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")

class post(models.Model):
    author = models.CharField(max_length=200,default="x")
    title = models.CharField(max_length=200,default="x")
    mood = models.CharField(max_length=200,default="x")
    price = models.DecimalField(max_digits=20,decimal_places=0) 