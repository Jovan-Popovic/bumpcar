from django.contrib import admin
from .models import Profile, Vehicle, Image
from .model_fields import (
    VehicleType,
    Drivetrain,
    Condition,
    Location,
    FuelType,
    GearType,
    Color,
    Brand,
    BrandModel,
)


admin.site.register(Profile)
admin.site.register(Vehicle)

admin.site.register(VehicleType)
admin.site.register(Drivetrain)
admin.site.register(BrandModel)
admin.site.register(Condition)
admin.site.register(FuelType)
admin.site.register(GearType)
admin.site.register(Location)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Image)


