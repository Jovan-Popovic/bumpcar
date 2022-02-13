from rest_framework import serializers
from base.models import Vehicle, Profile
from django.contrib.auth.models import User


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'email', 'password', 'username']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['location', 'phone', 'user', 'id']

    def create(self, validated_data):
        user_data=validated_data.pop('user')
        this_user = User.objects.create_user(**user_data)
        new_clien = Profile(user=this_user)
        new_clien.save()
        return new_clien