from django.contrib import admin
from .models import Profile, Vehicle
from .model_fields import Condition

admin.site.register(Profile)
admin.site.register(Vehicle)

class ConditionAdmin(admin.ModelAdmin):
    list_display = ("value", "id")

admin.site.register(Condition, ConditionAdmin)


# Register your models here.
