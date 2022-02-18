from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Profile, Vehicle
from .model_fields import (
    VehicleType,
    Drivetrain,
    Condition,
    FuelType,
    GearType,
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
        auth_user = self.context['request'].user
        profile_id = self.context['request'].parser_context.get('kwargs').get('pk')

        if auth_user.id == profile_id or auth_user.is_superuser or auth_user.is_staff:
            Profile.objects.filter(user = profile_id).update(**validated_data)

            for key in validated_data:
                setattr(instance, key, validated_data.get(key))

        return instance


### Vehicle Serializers ###

class GetVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class CreateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'name',
            'price',
            'year',
            'horse_power',
            'seat_count',
            'vehicle_type',
            'drivetrain',
            'fuel_type',
            'gear_type',
            'condition',
            'color',
            'brand',
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        vehicle = Vehicle.objects.create(**validated_data)
        return vehicle


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

