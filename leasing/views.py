from rest_framework import viewsets, filters
from leasing.serializers import *
from leasing.pagination import *
# Create your views here.


class VehicleViewset(viewsets.ModelViewSet):
    queryset = VehicleDetails.objects.all()
    serializer_class = VehicleDetailsSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['year']
    lookup_field = 'vin'

    def get_queryset(self):
        qs = super().get_queryset()
        vehicle_type = str(self.request.query_params.get('type')).lower()
        make = str(self.request.query_params.get('make')).lower()
        if vehicle_type in ['car', 'motorcycle', 'truck']:
            vehicleType = None
            for value in VehicleType.choices:
                if value[1].lower() == vehicle_type:
                    vehicleType = value[0]
            if vehicleType:
                return qs.filter(vehicle_type=vehicleType)
        if make != "none" and isinstance(make, str):
            return qs.filter(make__contains=make)
        return qs
