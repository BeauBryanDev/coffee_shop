from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order


# Create your views here.
class MYOrderslist(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    queryset = Order.objects.filter(is_active=True).order_by('-created_at')
    
    def get_object(self, queryset=None):
        return super().get_object(queryset=queryset)


class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'pk'
    queryset = Order.objects.filter(is_active=True)
    