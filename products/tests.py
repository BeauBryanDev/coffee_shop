from django.test import TestCase
from .models import Product
from django.urls import reverse

# Create your tests here.

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=10,
            product_image="https://example.com/test.jpg",
        )   
        
    def test_product_str(self):
 
        self.assertEqual(str(self.product), "Test Product - $10.00 - Stock: 10")


class ProductListViewTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=10,
            product_image="https://example.com/test.jpg",
        )   
        
    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    
    def test_product_detail_view(self):
        response = self.client.get(reverse("product_detail", args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)    