
from time import timezone
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, default="non genre")

    def __str__(self):
        return self.email


class Location(models.Model):
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    zip = models.IntegerField()
    
    def __str__(self):
        return self.city

class Stadium(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stadiums')
    name = models.CharField(max_length=100)
    photo= models.TextField(default='')

    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='stadiums')
    reserved_start_date = models.DateTimeField()
    reserved_end_date = models.DateTimeField()
    time = models.CharField(max_length=10)
    
