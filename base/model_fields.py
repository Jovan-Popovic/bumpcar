from django.db import models

class Condition(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value

# class FuelType(models.Model):
#     value = models.CharField(max_length=10)

#     def __str__(self):
#         return self.value