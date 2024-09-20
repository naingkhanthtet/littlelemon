from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_create(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 10)

    def test_delete(self):
        item = Menu.objects.get(id=self.item.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)
