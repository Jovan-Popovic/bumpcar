from django.contrib import admin
from .models import Profile, Vehicle
from .model_fields import (
    VehicleType,
    Drivetrain,
    Condition,
    FuelType,
    GearType,
    Color,
    Brand,
)


admin.site.register(Profile)
admin.site.register(Vehicle)

admin.site.register(VehicleType)
admin.site.register(Drivetrain)
admin.site.register(Condition)
admin.site.register(FuelType)
admin.site.register(GearType)
admin.site.register(Color)
admin.site.register(Brand)

