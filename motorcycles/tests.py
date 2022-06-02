from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Motorcycle


class MotorcycleTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_thing = Motorcycle.objects.create(
            owner=testuser1,
            make='Suzuki',
            year='2016',
            model='GSXR',
        )
        test_thing.save()

    def test_motorcycle_model(self):
        motorcycle = Motorcycle.objects.get(id=1)
        actual_owner = str(motorcycle.owner)
        actual_make = str(motorcycle.make)
        actual_year = str(motorcycle.year)
        actual_model = str(motorcycle.model)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_make, "Suzuki")
        self.assertEqual(actual_year, '2016')
        self.assertEqual(actual_model, 'GSXR')

    def test_get_motorcycle_list(self):
        url = reverse("motorcycle_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        motorcycle = response.data
        self.assertEqual(len(motorcycle), 1)
        self.assertEqual(motorcycle[0]["make"], "Suzuki")

    def test_get_motorcycle_by_id(self):
        url = reverse("motorcycle_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        motorcycle = response.data
        self.assertEqual(motorcycle["make"], "Suzuki")

    def test_create_motorcycle(self):
        url = reverse("motorcycle_list")
        data = {'owner': 1, 'make': 'Suzuki', "year": '2016', 'model': 'GSXR'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        motorcycle = Motorcycle.objects.all()
        self.assertEqual(len(motorcycle), 2)
        self.assertEqual(Motorcycle.objects.get(id=2).make, "Suzuki")

    def test_update_motorcycle(self):
        url = reverse("motorcycle_detail", args=(1,))
        data = {
            "owner": 1,
            "make": "Yamaha",
            "model": "YZFR6",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        motorcycle = Motorcycle.objects.get(id=1)
        self.assertEqual(motorcycle.make, data["make"])
        self.assertEqual(motorcycle.owner.id, data["owner"])
        self.assertEqual(motorcycle.model, data["model"])

    def test_delete_motorcycle(self):
        url = reverse("motorcycle_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        motorcycle = Motorcycle.objects.all()
        self.assertEqual(len(motorcycle), 0)

    # class 33
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("motorcycle_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)