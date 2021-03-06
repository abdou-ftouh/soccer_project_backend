
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    gendre = models.CharField(max_length=20)
    def __str__(self):
        return self.email


class Location(models.Model):
    city = models.CharField(max_length=50, unique=True)
  
    
   

class Stadium(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stadiums')
    name = models.CharField(max_length=100)
    photo= models.TextField()
    address = models.CharField(max_length=200)
    description = models.TextField(default='This is a mixed gender league that takes place weekly on Fridays.')
    zip = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='reservations')
    reserved_start_date = models.DateTimeField()
    reserved_end_date = models.DateTimeField()


    
