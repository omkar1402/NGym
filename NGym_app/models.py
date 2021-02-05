from django.db import models
from django import forms

# Create your models here.
class Choices(models.Model):
    choices = models.CharField(max_length=50,default=None)

    def __str__(self):
        return self.choices

class Calories1(models.Model):
    Name=models.CharField(max_length=100,default=None, blank=True)
    Weight = models.IntegerField( blank=True)
    Height = models.IntegerField( blank=True)
    Age=models.IntegerField( blank=True)
    Choices = models.ForeignKey(Choices,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)