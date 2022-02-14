from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerProfileOrReadOnly

from django.views.generic import DetailView
from base.models import Vehicle, Profile
from .serializers import UserSerializer, ProfileSerializer, VehicleSerializer, GetVehicleSerializer

### User - views ###
class CreateUser(generics.CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = [AllowAny]

class ListUser(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = [AllowAny]

class GetUser(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    def get(self, request):
        print(request.data)
        user_id = Profile.objects.get(user_id=1)
        return Profile.objects.get(id = user_id)


### Vehicle - views ###
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


class CreateVehicle(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
