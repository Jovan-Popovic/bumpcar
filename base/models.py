from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .model_fields import Condition


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField(max_length=96)
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.email


class Vehicle(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=90)
    price = models.IntegerField()
    year = models.IntegerField()
    horse_power = models.IntegerField()
    seat_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Accessories(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     name = models.CharField(max_length=90)
#     price = models.IntegerField()
#     year = models.IntegerField()

#     def __str__(self):
#         return self.name
