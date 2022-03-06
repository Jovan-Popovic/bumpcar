from rest_framework import generics, status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.views.generic import DetailView
from .serializers import *

### User - views ###

class UserView():
    @method_decorator(csrf_exempt, name='dispatch')
    class CreateUser(generics.CreateAPIView):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer
        permission_classes = [AllowAny]

    class GetUser(generics.ListAPIView):
        serializer_class = ProfileSerializer
        permission_classes = [AllowAny]

        def get_queryset(self):
            user = User.objects.get(username = self.kwargs['username'])
            queryset = Profile.objects.filter(user = user)
            return queryset

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
        permission_classes = [IsAuthenticated]

        def destroy(self, request, *args, **kwargs):
            auth_user =  request.user # Logged User pk
            user_to_delete = kwargs.get('pk') # deleting pk

            User.objects.get(pk = auth_user.pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            # return Response(status=status.HTTP_403_FORBIDDEN)


### Vehicle - views ###

class VehicleView():
    class CreateVehicle(generics.CreateAPIView):
        queryset = Vehicle.objects.all()
        permission_classes = [AllowAny]
        serializer_class = CreateVehicleSerializer

    class VehicleListAll(generics.ListAPIView):
        serializer_class = GetVehicleSerializer
        permission_classes = [AllowAny]

        def get_queryset(self):
            vehicles = Vehicle.objects.all()
            get_request = self.request.GET.get

            value = get_request('brand', '').split(',') ### Brand Check
            vehicles = vehicles.filter(brand__in=value) if value != [''] else vehicles

            value = get_request('model', '').split(',') ### Model Check
            vehicles = vehicles.filter(brand_model__in=value) if value != [''] else vehicles

            value = get_request('fuel-type', '').split(',') ### Fuel Type Check
            vehicles = vehicles.filter(fuel_type_id__in=value) if value != [''] else vehicles

            value = get_request('color', '').split(',') ### Color Check
            vehicles = vehicles.filter(color__in=value) if value != [''] else vehicles

            value = get_request('condition', '').split(',') ### Condition Check
            vehicles = vehicles.filter(condition__in=value) if value != [''] else vehicles

            value = get_request('drivetrain', '').split(',') ### Drivetrain Check
            vehicles = vehicles.filter(drivetrain__in=value) if value != [''] else vehicles

            value = get_request('gear-type', '').split(',') ### Gear Type Check
            vehicles = vehicles.filter(gear_type__in=value) if value != [''] else vehicles

            value = get_request('year', '').split(',') ### Check for year
            vehicles = vehicles.filter(year__in=value) if value != [''] else vehicles

            value = get_request('vehicle-type', '').split(',') ### Gear Type Check
            vehicles = vehicles.filter(vehicle_type__in=value) if value != [''] else vehicles

            value = get_request('min-price', 0) ### Maximum price check
            vehicles = vehicles.filter(price__gt = int(value)-1)

            value = get_request('max-price', None) ### Minimum price check
            vehicles = vehicles.filter(price__lt = int(value)+1) if value != None else vehicles

            value = get_request('seat-count', '').split(',')
            vehicles = vehicles.filter(seat_count__in=value) if value != [''] else vehicles

            value = get_request('location', '').split(',') ### Minimum price check
            vehicles = vehicles.filter(location__in = value) if value != [''] else vehicles

            value = get_request('user', None) ### User Check
            vehicles = vehicles.filter(user_id=value) if value != None else vehicles

            value = get_request('name-search', '')
            vehicles = vehicles.filter(name__icontains = value)

            limit = int(get_request('limit', 10))
            offset = int(get_request('offset', 0))
            vehicles = vehicles[offset:offset+limit]

            return vehicles

    class GetVehicleById(generics.RetrieveAPIView):
        queryset = Vehicle.objects.all()
        serializer_class = GetVehicleSerializer
        lookup_field = 'pk'
        permission_classes = [AllowAny]

    class GetVehicleByUser(generics.ListAPIView):
        serializer_class = GetVehicleSerializer
        permission_classes = [AllowAny]

        def get_queryset(self):
            user = User.objects.get(username = self.kwargs['username'])
            vehicles = Vehicle.objects.filter(user = user)
            return vehicles

    class DeleteVehicle(generics.DestroyAPIView):
        queryset = Profile.objects.all()
        permission_classes = [IsAuthenticated]

        def destroy(self, request, *args, **kwargs):
            auth_user = request.user
            # vehicle_to_delete = kwargs
            vehicle_to_delete = kwargs.get('pk')
            vehicles_user = Vehicle.objects.get(pk = kwargs.get('pk')).user_id

            if auth_user.pk == vehicles_user or auth_user.is_superuser or auth_user.is_staff:
                Vehicle.objects.get(pk = vehicle_to_delete).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_403_FORBIDDEN)


class GetImageById(generics.ListAPIView):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer
        lookup_field = 'vehicle'
        permission_classes = [AllowAny]

        def get_queryset(self):
            vehicle = self.kwargs['vehicle']
            queryset = Image.objects.all()
            queryset = queryset.filter(vehicle=vehicle)
            return queryset

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

class ListModels(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = FieldSerizalizer

    def get_queryset(self):
        queryset = BrandModel.objects.all()
        queryset = queryset.filter(brand_id = self.kwargs['fk'])
        return queryset

class Locations(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()