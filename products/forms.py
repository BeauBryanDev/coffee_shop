from django import forms 
from .models import Product


# Products Forms

class ProductForm( forms.Form ) :
    
    name = forms.CharField(max_length=64, label="Product_Name")
    description = forms.CharField(widget=forms.Textarea, max_length=255, label="Product_Description")
    price = forms.DecimalField(max_digits=8, decimal_places=2, label="Product_Price")
    stock = forms.IntegerField(label="Stock")
    available = forms.BooleanField(required=False, initial=True, label="Available")
    product_image = forms.URLField(max_length=200, required=False, label="Product_Image")
    category = forms.CharField(max_length=32, label="Product_Category")
    
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price    
    
    def save(self):
        
        product = Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            stock=self.cleaned_data['stock'],
            available=self.cleaned_data['available'],       
            product_image=self.cleaned_data.get('product_image', ''),
            category=self.cleaned_data['category'],
        )
        return product