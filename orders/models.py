from django.db import models
from django.conf import settings

# Create your models here.

#create Order model to store order details
class Order(models.Model):
    
    # optional link to the authenticated user who placed the order
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='orders'
    )

    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Order {self.order_number} -{self.is_active} by {self.customer_name}" 
    

class ProductOrder(models.Model):
    
    order = models.ForeignKey(Order, related_name='product_orders', on_delete=models.CASCADE)
    product_name = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"{self.quantity} x {self.product_name} for Order {self.order.order_number}"