from rest_framework import serializers
from base.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ("id", "name", "price", "year", "horse_power", "seat_count", "created_at")
