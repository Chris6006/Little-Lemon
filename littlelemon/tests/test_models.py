from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(Title="TestIceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "TestIceCream : 80")

class MenuViewTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="TestIceCream", Price=90, Inventory=100)
        self.assertEqual(str(item), "TestIceCream : 80")