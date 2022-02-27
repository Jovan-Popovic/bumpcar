from django.db import models

class Condition(models.Model):
    value = models.CharField(max_length=10, primary_key = True)

    def __str__(self):
        return self.value

class FuelType(models.Model):
    value = models.CharField(max_length=150, primary_key = True)

    def __str__(self):
        return self.value


class GearType(models.Model):
    value = models.CharField(max_length=150, primary_key = True)

    def __str__(self):
        return self.value


class Color(models.Model):
    value = models.CharField(max_length=150, primary_key = True)

    def __str__(self):
        return self.value


class VehicleType(models.Model):
    value = models.CharField(max_length=100, primary_key = True)

    def __str__(self):
        return self.value


class Drivetrain(models.Model):
    value = models.CharField(max_length=150, primary_key = True)

    def __str__(self):
        return self.value

class Brand(models.Model):
    value = models.CharField(max_length=150, primary_key = True)

    def __str__(self):
        return self.value

class BrandModel(models.Model):
    value = models.CharField(max_length=150, primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

class Location(models.Model):
    value = models.CharField(max_length=150, primary_key=True)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)

    def __str__(self):
        return self.value