from django.db import models


class VehicleType(models.TextChoices):
    CAR = 'C', 'Car'
    TRUCK = 'T', 'Truck'
    MOTORCYCLE = 'M', 'Motorcycle'


class VehicleDetails(models.Model):
    vin = models.CharField(max_length=15, unique=True, null=False, blank=False)
    vehicle_type = models.CharField(max_length=2, choices=VehicleType.choices, default=VehicleType.CAR)
    make = models.CharField(max_length=15, null=False, blank=False)
    model = models.CharField(max_length=15, null=False, blank=False)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    seat_capacity = models.PositiveBigIntegerField(blank=True, null=True)
    roof_rack_availability = models.BooleanField(default=False)
    haul_capacity = models.PositiveBigIntegerField(blank=True, null=True)
    sidecar_availability = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

