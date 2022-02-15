from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.generic import DetailView

from base.models import Vehicle, Profile, Condition
from .serializers import (
    ProfileSerializer,
    CreateVehicleSerializer,
    GetVehicleSerializer,
    ConditionSerizalizer
)

### User - views ###

class UserView():
    class CreateUser(generics.CreateAPIView):
        queryset=Profile.objects.all()
        serializer_class=ProfileSerializer
        permission_classes = [AllowAny]

    class ListUser(generics.ListAPIView):
        queryset=Profile.objects.all()
        serializer_class=ProfileSerializer
        permission_classes = [AllowAny]


### Vehicle - views ###

class VehicleView():
    class CreateVehicle(generics.CreateAPIView):
        queryset = Vehicle.objects.all()
        serializer_class = CreateVehicleSerializer
        permission_classes = [IsAuthenticated]

    class VehicleListAll(generics.ListAPIView):
        serializer_class = GetVehicleSerializer
        permission_classes = [AllowAny]

        def get_queryset(self):
            vehicles = Vehicle.objects.all()

            limit = self.request.GET.get('limit', None)
            offset = self.request.GET.get('offset', 0)
            if limit is not None:
                limit = int(limit)
                offset = int(offset)
                vehicles = vehicles[offset:offset+limit]

            return vehicles

    class GetVehicleById(generics.RetrieveAPIView):
        queryset = Vehicle.objects.all()
        serializer_class = GetVehicleSerializer
        lookup_field = 'pk'
        permission_classes = [AllowAny]


### Helper Models ###

class ConditionView():
    class CreateCondition(generics.CreateAPIView):
        queryset = Condition.objects.all()
        permission_classes = [IsAuthenticated]
        serializer_class = ConditionSerizalizer

    class GetAllCondition(generics.ListAPIView):
        queryset = Condition.objects.all()
        serializer_class = ConditionSerizalizer
        permission_classes = [AllowAny]

