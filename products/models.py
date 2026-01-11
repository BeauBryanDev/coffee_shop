from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64 , verbose_name="Product Name") 
    description = models.TextField( max_length=255, verbose_name="Product Description")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Product Price")
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    product_image = models.URLField(max_length=200, null=True, blank=True, verbose_name="Product Image")
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    category = models.CharField(max_length=32, verbose_name="Product Category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - ${self.price} - Stock: {self.stock}"