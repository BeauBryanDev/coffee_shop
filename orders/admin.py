from django.contrib import admin
from .models import Order, ProductOrder


class orderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'customer_email', 'is_active', 'created_at', 'updated_at')
    search_fields = ('order_number', 'customer_name', 'customer_email')
    list_filter = ('is_active', 'created_at')

# Register your models here.
admin.site.register(Order, orderAdmin)
admin.site.register(ProductOrder)