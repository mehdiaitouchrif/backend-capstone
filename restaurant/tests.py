from django.test import TestCase
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=50, inventory=100)
        self.assertEqual(item.__str__(), 'IceCream')


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name='Test', no_of_guests=5)
        self.assertEqual(item.__str__(), 'Test')


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Pizza', price=10, inventory=10)
        self.menu2 = Menu.objects.create(title='Burger', price=8, inventory=40)

    def test_getall(self):
        url = '/restaurant/menu/'
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_single(self):
        url = f'/restaurant/menu/{self.menu1.id}'
        response = self.client.get(url)
        menu = Menu.objects.get(pk=self.menu1.id)
        serializer = MenuSerializer(menu)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

