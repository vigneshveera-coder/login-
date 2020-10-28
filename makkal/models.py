from django.db import models
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.

class post(models.Model):
    name=models.CharField(max_length=50)
    comment=models.TextField()
    def __str__(self):
        return self.name

class securty(models.Model):
    objects = None
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=40)
    def __str__(self):
        return self.name

    


