from rest_framework import serializers
from base.models import Vehicle, Profile


class UserSerializer(serializers.ModelSerializer):
    profile=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Profile
        fields='__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ("id", "name", "price", "year", "horse_power", "seat_count", "created_at")

