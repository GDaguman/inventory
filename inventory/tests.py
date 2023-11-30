from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

class InventoryTestCase(TestCase):
    def test_inventory_list_page_status(self):
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page_status(self):
        response = self.client.get(reverse('inventory_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
