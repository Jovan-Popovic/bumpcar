from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.views.generic import DetailView
from .serializers import *

### User - views ###

class UserView():
    class CreateUser(generics.CreateAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer
        permission_classes = [AllowAny]

    class ListUser(generics.ListAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer
        permission_classes = [AllowAny]

    class UpdateUser(generics.UpdateAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileUpdateSerializer
        permission_classes = [IsAuthenticated]
        lookup_field = 'pk'

    class DeleteUser(generics.DestroyAPIView):
        queryset = Profile.objects.all()
        permission_classes = [AllowAny]

        def destroy(self, request, *args, **kwargs):
            auth_user =  request.user # Logged User pk
            user_to_delete = kwargs.get('pk') # deleting pk

            if auth_user.pk == user_to_delete or auth_user.is_superuser or auth_user.is_staff:
                User.objects.get(pk = auth_user.pk).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_403_FORBIDDEN)


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


class ListFieldValues(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FieldSerizalizer

    def get_queryset(self):
        queryset = self.kwargs['model'].objects.all()
        return queryset
