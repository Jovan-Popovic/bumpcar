from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.views.generic import DetailView
from .serializers import *

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
            get_request = self.request.GET.get

            value = get_request('brand', None) ### Brand Check
            vehicles = vehicles.filter(brand=value) if value != None else vehicles

            value = get_request('fuel-type', None) ### Fuel Type Check
            vehicles = vehicles.filter(fuel_type_id=value) if value != None else vehicles

            value = get_request('color', None) ### Color Check
            vehicles = vehicles.filter(color_id=value) if value != None else vehicles

            value = get_request('condition', None) ### Condition Check
            vehicles = vehicles.filter(condition_id=value) if value != None else vehicles

            value = get_request('drivetrain', None) ### Drivetrain Check
            vehicles = vehicles.filter(drivetrain_id=value) if value != None else vehicles

            value = get_request('gear-type', None) ### Gear Type Check
            vehicles = vehicles.filter(gear_type_id=value) if value != None else vehicles

            value = get_request('vehicle-type', None) ### Gear Type Check
            vehicles = vehicles.filter(vehicle_type_id=value) if value != None else vehicles

            value = get_request('user', None) ### User Check
            vehicles = vehicles.filter(user_id=value) if value != None else vehicles

            limit = int(get_request('limit', 10))
            offset = int(get_request('offset', 0))
            vehicles = vehicles[offset:offset+limit]

            return vehicles

    class GetVehicleById(generics.RetrieveAPIView):
        queryset = Vehicle.objects.all()
        serializer_class = GetVehicleSerializer
        lookup_field = 'pk'
        permission_classes = [AllowAny]


### Field Models ###

class CreateField(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = FieldSerizalizer

    def get_queryset(self):
        queryset = self.kwargs['model'].objects.all()
        return queryset


class GetAllFieldValues(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FieldSerizalizer

    def get_queryset(self):
        queryset = self.kwargs['model'].objects.all()
        return queryset
