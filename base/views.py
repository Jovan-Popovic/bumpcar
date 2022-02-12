from rest_framework import generics
from django.shortcuts import get_object_or_404

from base.models import Vehicle
from base.serializers import VehicleSerializer


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