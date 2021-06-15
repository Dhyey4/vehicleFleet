from django.test import TestCase
from .models import VehicleDetails
from rest_framework.test import APIClient
from rest_framework import status


class ModelTestCase(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.vin = "100"
        self.vehicleType = "C"
        self.make = "car"
        self.model = "car1"
        self.year = 2013
        self.seat_capacity = 2
        self.vehicleData = VehicleDetails(vin=self.vin, vehicle_type=self.vehicleType, make=self.make,
                                         model=self.model, year=self.year, seat_capacity=self.seat_capacity)

    def test_model_can_create_a_vehicle(self):
        """Test the VehicleDetails model can create a Vehicle ."""
        old_count = VehicleDetails.objects.count()
        self.vehicleData.save()
        new_count = VehicleDetails.objects.count()
        self.assertNotEqual(old_count, new_count)


class APIViewTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.content_type = 'application/json'
        self.car = VehicleDetails.objects.create(vin="102", vehicle_type="C", make="car1",
                       model="car11", year=2001, seat_capacity=4)
        self.bike = VehicleDetails.objects.create(vin="103", vehicle_type="M", make="bike1",
                                                 model="bike2", year=2002, seat_capacity=2)
        self.truck = VehicleDetails.objects.create(vin="104", vehicle_type="T", make="truck",
                                                 model="truck1", year=2003, seat_capacity=10)

    def test_api_can_create_a_vehicle(self):
        """Test the api has bucket creation capability."""
        vehicle_data = {
            "vehicle_type": "motorcycle",
            "vin": "116",
            "make": "bike3",
            "model": "bike44",
            "year": 2015,
            "seat_capacity": 2,
            "roof_rack_availability": False,
            "haul_capacity": None,
            "sidecar_availability": True
        }
        response = self.client.post('/api/vehicle/', vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_get_list_of_vehicle(self):
        response = self.client.get('/api/vehicle/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_get_list_of_vehicle_count(self):
        response = self.client.get('/api/vehicle/', format='json')
        self.assertEqual(response.json()["count"], 3)

    def test_api_get_list_of_vehicle_filter_by_type_car(self):
        response = self.client.get('/api/vehicle/?type=car', format='json')
        self.assertEqual(response.json()["count"], 1)

    def test_api_get_list_of_vehicle_filter_by_type_motorcycle(self):
        response = self.client.get('/api/vehicle/?type=motorcycle', format='json')
        self.assertEqual(response.json()["count"], 1)

    def test_api_get_list_of_vehicle_filter_by_type_truck(self):
        response = self.client.get('/api/vehicle/?type=truck', format='json')
        self.assertEqual(response.json()["count"], 1)

    def test_api_get_list_of_vehicle_filter_by_make(self):
        response = self.client.get('/api/vehicle/?make=car', format='json')
        self.assertEqual(response.json()["count"], 1)

    def test_api_get_list_of_vehicle_order_by_year(self):
        response = self.client.get('/api/vehicle/?ordering=year', format='json')
        self.assertEqual(response.json()["results"][0]["year"], self.car.year)

    def test_api_get_vehicle_by_vin(self):
        response = self.client.get('/api/vehicle/102/', format='json')
        self.assertEqual(response.json()["vin"], self.car.vin)

    def test_api_update_vehicle_data_using_vin(self):
        vehicle_data = {
            "vehicle_type": "car",
            "vin": "102",
            "make": "bike3",
            "model": "bike44",
            "year": 2015,
            "seat_capacity": 2,
            "roof_rack_availability": False,
            "haul_capacity": None,
            "sidecar_availability": True
        }
        response = self.client.put('/api/vehicle/102/', vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_delete_vehicle_using_vin(self):
        response = self.client.delete('/api/vehicle/102/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/vehicle/', format='json')
        self.assertEqual(response.json()["count"], 2)

