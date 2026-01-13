from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .views import MYOrderslist
from .models import Order, ProductOrder
from products.models import Product

User = get_user_model()

class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser_order",
            password="testpassword",
            email="test@example.com"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=10,
            product_image="https://example.com/test.jpg"
        )
        self.order = Order.objects.create(
            user=self.user,
            order_number="1234567890",
            customer_name="Test Customer",
            customer_email="test@example.com",
            is_active=True,
        )
        self.product_order = ProductOrder.objects.create(
            order=self.order,
            product_name=self.product,
            quantity=1,
            price_per_item=10.00,
        )

    def test_order_str(self):
        self.assertEqual(str(self.order), "Order 1234567890 -True by Test Customer")

    def test_product_order_str(self):
        # ProductOrder __str__: f"{self.quantity} x {self.product_name} for Order {self.order.order_number}"
        # Product __str__: f"{self.name} - ${self.price} - Stock: {self.stock}"
        expected_str = f"1 x Test Product - $10.00 - Stock: 10 for Order 1234567890"
        self.assertEqual(str(self.product_order), expected_str)

    def test_order_list_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("order_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.order_number)
        
            
    def test_order_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("order_details", args=[self.order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.order_number)


class MyOrderViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="user@test.com"
        )
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            stock=10,
            product_image="https://example.com/test.jpg"
        )
        self.order = Order.objects.create(
            user=self.user,
            order_number="1234567890",
            customer_name="Test Customer",
            customer_email="test@example.com",
            is_active=True,
        )
        self.product_order = ProductOrder.objects.create(
            order=self.order,
            product_name=self.product,
            quantity=1,
            price_per_item=10.00,
        )
        self.my_order_view = MYOrderslist.as_view()

    def test_my_order_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("order_list")) # Assuming order_list is the name for my_order_view
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.order_number)
    