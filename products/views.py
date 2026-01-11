from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView , TemplateView , FormView
from django.core.paginator import Paginator

from .models import Product
from .forms import ProductForm

# Create your views here.

class home(TemplateView):
    template_name = 'products/home.html'
    

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10    
    ordering = ['-created_at']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
    
class ProductFormView( FormView ):  
    
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list') 
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
    
    
    
"""
mocha coffee adddress
https://hoxtoncoffee.com/cdn/shop/articles/latte-art-on-mocha_1200x1200.jpg?v=1660069726

Expreso Coffee address
https://www.cafe-mx.com/blog/app/assets/media/2018/08/cafe-expreso.jpg

capuchino coffee 
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfPhPty83awEZiMFjBwtr4qai6J1evVnn7Vg&s

cold brew 
https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKPhK6VkiP1hWTryv_ZW_NvQsqAQ48VQRIug&s

Ice latte
https://markieskitchen.com/wp-content/uploads/2022/07/iced-mocha-latte-4.jpg

"""