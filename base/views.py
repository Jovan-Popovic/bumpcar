from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from base.models import Vehicle, Profile
from base.serializers import VehicleSerializer
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserSerializer, ProfileSerializer

class VehicleListAll(generics.ListAPIView):
    serializer_class = VehicleSerializer

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
    serializer_class = VehicleSerializer
    lookup_field = 'pk'


class CreateUser(generics.CreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = [AllowAny]

class ListUser(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = [AllowAny]
