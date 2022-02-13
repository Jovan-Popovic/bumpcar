from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from base.models import Vehicle, Profile
from base.serializers import VehicleSerializer
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserSerializer

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

# class DeleteVehicleById(generics.DestroyAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer
#     lookup_field = 'pk'



class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class userProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]