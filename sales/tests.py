import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# models
from sales.models import Sale, Saler, ItemSale
from customers.models import Customer
from products.models import Product

class SaleTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.customer = Customer.objects.create(name='renan test', email='emailtest@tes.com', phone='8898989899')
        self.saler = Saler.objects.create(name='renan saler test', email='emailtessalet@tes.com', phone='8854989899')
        self.product = Product.objects.create(code=2121, description='testee3', value_unit=123, commission=2)
        self.item_sale = ItemSale.objects.create(product=self.product, amount=3)


    def test_create_sale(self):
        sale_data = {"invoice": 3234, "date": "2023-06-05", "customer": self.customer.pk, "saler": self.saler.pk,
                          "products": [self.product.pk]}
        response = self.client.post('/api/v1/sales/', sale_data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Sale.objects.count(), 1)
        self.assertEquals(Sale.objects.get().pk, 1)

    def test_list_sale(self):
        sale = Sale.objects.create(
            invoice=2198,
            date="2023-06-05",
            customer=self.customer,
            saler=self.saler,
        )
        sale.products.set([self.item_sale.pk])
        response = self.client.get('/api/v1/sales/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)

    def test_retrieve_sale(self):
        sale = Sale.objects.create(
            invoice=2198,
            date="2023-06-05",
            customer=self.customer,
            saler=self.saler,
        )
        sale.products.set([self.item_sale.pk])
        response = self.client.get(f'/api/v1/sales/{sale.pk}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['invoice'], 2198)
