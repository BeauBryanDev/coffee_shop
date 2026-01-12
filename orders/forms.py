from django.forms import ModelForm
from .models import Order, ProductOrder

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'customer_name', 'customer_email', 'is_active']
        
        
class ProductOrderForm(ModelForm):
    class Meta:
        model = ProductOrder
        fields = ['product_name', 'quantity', 'price_per_item']
        # Note: 'order' is NOT included here - it's created in the view