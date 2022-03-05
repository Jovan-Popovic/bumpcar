from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from .model_fields import (
    VehicleType,
    Drivetrain,
    Condition,
    FuelType,
    GearType,
    Location,
    Color,
    Brand,
    BrandModel,
)

FEATURES = (('Power Steering', 'Power Steering'), ('AC', 'AC'), ('Alarm', 'Alarm'), ('Bluetooth', 'Bluetooth'),
            ('Heated Seats', 'Heated Seats'), ('Wifi', 'Wifi'), ('Cruise Control', 'Cruise Control'), ('Front Parking Sensor', 'Front Parking Sensor'),
            ('Rear Parking Sensor', 'Rear Parking Sensor'), ('Roof Rack', 'Roof Rack'), ('Power Window', 'Power Window'), ('Sunroof', 'Sunroof'),
            ('USB Port', 'USB Port'), ('Sound System', 'Sound System'), ('Memory Seat', 'Memory Seat'), ('Other', 'Other'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField(max_length=96)
    location = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.email


class Vehicle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    vehicle_type    = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    drivetrain      = models.ForeignKey(Drivetrain, on_delete=models.CASCADE)
    condition       = models.ForeignKey(Condition, on_delete=models.CASCADE)
    fuel_type       = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    gear_type       = models.ForeignKey(GearType, on_delete=models.CASCADE)
    color           = models.ForeignKey(Color, on_delete=models.CASCADE)
    brand           = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_model     = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)

    name            = models.CharField(max_length=90)
    price           = models.IntegerField()
    year            = models.IntegerField()
    horse_power     = models.IntegerField()
    seat_count      = models.IntegerField()

    milage          = models.IntegerField(default=0)
    engine_capacity = models.IntegerField(default=0)
    length          = models.IntegerField(default=0)
    width           = models.IntegerField(default=0)
    height          = models.IntegerField(default=0)
    cargo_volume    = models.IntegerField(default=0)

    description     = models.CharField(max_length = 2000, default='')

    features    = MultiSelectField(choices=FEATURES, default=None)

    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="./img/")
