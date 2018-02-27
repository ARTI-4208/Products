from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product

class AccountTests(APITestCase):
    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'id': '550e8400-e29b-41d4-a716-446655440000',
            'name': 'Lampara',
            'description': 'Lamparas a la medida',
            'brand': 'Iluminar',
            'idprovider': 45
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Lampara')
