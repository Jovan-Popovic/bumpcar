from rest_framework import serializers
from base.models import Vehicle, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields=['email', 'password', 'username']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'location', 'phone', 'full_name', 'id']

    def create(self, validated_data):
        user_data=validated_data.pop('user')
        this_user = User.objects.create_user(**user_data)
        profile_data = {}

        profile_data["phone"] = validated_data.pop('phone') if "phone" in validated_data else ""
        profile_data["location"] = validated_data.pop('location') if "phone" in validated_data else ""

        new_profile = Profile(
            user=this_user,
            phone = profile_data["phone"],
            location = validated_data["location"],
            )

        new_profile.save()
        return new_profile

class GetVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['name', 'price', 'year', 'horse_power', 'seat_count']

    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        vehicle = Vehicle.objects.create(**validated_data)
        return vehicle