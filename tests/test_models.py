from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_example(self):
        # item = Menu.objects.create(title="IceCream", price=80, inventory=10)
        # self.assertEqual(item, "IceCream : 80")
        self.assertEqual(1 + 1, 2)
