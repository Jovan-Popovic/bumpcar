from django.db import models


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
