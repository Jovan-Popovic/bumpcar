from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=96)
    email = models.EmailField(max_length=254, unique=True)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.email

class Vehicle(models.Model):
    name = models.CharField(max_length=90)
    price = models.IntegerField(range(0, 1000000))
    year = models.IntegerField(range(1990, 2022))
    horse_power = models.IntegerField(range(1, 1500))
    seat_count = models.IntegerField(range(1, 50))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=90)
    price = models.IntegerField(range(0, 1000))
    year = models.IntegerField(range(1990 - 2022))

    def __str__(self):
        return self.name
