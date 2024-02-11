from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime

class MenuItemTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(Title="TestIceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "TestIceCream : 80")

class BookingTest(TestCase):

    def test_get_item(self):
        current_datetime = datetime.now()
        item = Booking.objects.create(Name="JohnTest", No_of_guests = 5, BookingDate = current_datetime)
        self.assertEqual(str(item), "JohnTest - " + current_datetime.strftime('%Y/%m/%d %H:%M:%S') + " - No. of Guests: " + str(5))