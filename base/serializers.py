from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from base.models import Profile, Vehicle, Image
from .model_fields import (
    VehicleType,
    Drivetrain,
    BrandModel,
    Condition,
    FuelType,
    GearType,
    Location,
    Color,
    Brand,
)


### User/Profile Serializers ###

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


class ProfileUpdateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateSerializer, self).__init__(*args, **kwargs)
        self.fields['location'].required = False
        self.fields['phone'].required = False
        self.fields['full_name'].required = False

    class Meta:
        model = Profile
        fields = ['location', 'phone', 'full_name']

    def update(self, instance, validated_data):
        profile_id = self.context['request'].parser_context.get('kwargs').get('pk')

        Profile.objects.filter(pk = profile_id).update(**validated_data)

        # for key in validated_data:
            # setattr(instance, key, validated_data.get(key))

        return instance


### Vehicle Serializers ###

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class GetVehicleSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='user.username')
    images = serializers.SerializerMethodField()

    def get_images(self, vehicle):
        queryset = Image.objects.filter(vehicle = vehicle)
        serializer = ImageSerializer(instance=queryset, many=True)
        return serializer.data
    class Meta:
        model = Vehicle
        fields = [
            'user',
            'created_by',
            'vehicle_type',
            'drivetrain',
            'condition',
            'fuel_type',
            'gear_type',
            'color',
            'brand',
            'brand_model',
            'location',
            'name',
            'price',
            'year',
            'horse_power',
            'seat_count',
            'milage',
            'engine_capacity',
            'length',
            'width',
            'height',
            'cargo_volume',
            'description',
            'features',
            'images',
            'id',
        ]

class VehicleMeta(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_type',
            'drivetrain',
            'condition',
            'fuel_type',
            'gear_type',
            'color',
            'brand',
            'brand_model',
            'location',
            'name',
            'price',
            'year',
            'horse_power',
            'seat_count',
            'features',
            'milage',
            'engine_capacity',
            'length',
            'width',
            'height',
            'cargo_volume',
            'description',
            'user',
        ]

class CreateVehicleSerializer(serializers.ModelSerializer):
    # vehicle = VehicleMeta()
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_type',
            'drivetrain',
            'condition',
            'fuel_type',
            'gear_type',
            'color',
            'brand',
            'brand_model',
            'location',
            'name',
            'price',
            'year',
            'horse_power',
            'seat_count',
            'features',
            'milage',
            'engine_capacity',
            'length',
            'width',
            'height',
            'cargo_volume',
            'description',
            'user',
        ]

    # def create(self, validated_data):
    #     vehicle_data = validated_data.get('vehicle')
    #     validated_data['user'] = self.context['request'].user
    #     new_vehicle = Vehicle.objects.create(**vehicle_data)
    #     new_vehicle.save()

    #     new_data = self.context['request'].FILES
    #     for img in new_data.getlist('image'):
    #         new_image = Image.objects.create(image=img, vehicle=new_vehicle)
    #         new_image.save()

    #     return validated_data


### Field model serializers ###

class FieldSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

    def create(self, validated_data):
        model_field = self.context.get('view').kwargs.get('model')
        new_value = model_field.objects.create(**validated_data)
        new_value.save()
        return new_value

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'