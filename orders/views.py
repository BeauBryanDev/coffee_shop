from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib import messages
from orders.models import Order, ProductOrder
from products.models import Product
from .forms import OrderForm, ProductOrderForm
import uuid
from datetime import datetime

# Create your views here.
class MYOrderslist(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    
    def get_queryset(self):
        """Return orders for the current user that are active, newest first."""
        return Order.objects.filter(is_active=True, user=self.request.user).order_by('-created_at')


class OrderDetail(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'pk'
    
    def get_queryset(self):
        """Limit detail view to active orders that belong to the requesting user."""
        return Order.objects.filter(is_active=True, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = OrderForm(instance=self.object)
        context['product_order_form'] = ProductOrderForm()
        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url =  reverse_lazy('order_list')
    
    def  form_valid(self, form):
        # Attach the current user before saving the order instance
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = self.get_form()
        return context
            
    
class CreateOrderProductView(LoginRequiredMixin, View):
    """Handle buying a product - creates Order and ProductOrder"""

    def get(self, request):
        """Display the product order form"""
        # Get product ID from query parameter
        product_id = request.GET.get('product_id')

        if product_id:
            product = get_object_or_404(Product, id=product_id)

            # Pre-fill form with product data
            form = ProductOrderForm(initial={
                'product_name': product.id,
                'price_per_item': product.price,
                'quantity': 1
            })

            return render(request, 'orders/product_order_form.html', {
                'product_order_form': form,
                'product': product
            })
        else:
            # No product specified
            form = ProductOrderForm()
            return render(request, 'orders/product_order_form.html', {
                'product_order_form': form
            })

    def post(self, request):
        """Handle the Buy Product button submission"""
        form = ProductOrderForm(request.POST)

        if form.is_valid():
            # Get the product
            product = form.cleaned_data['product_name']
            quantity = form.cleaned_data['quantity']
            price_per_item = form.cleaned_data['price_per_item']

            # Check if product has enough stock
            if product.stock < quantity:
                messages.error(request, f'Not enough stock! Only {product.stock} units available.')
                return render(request, 'orders/product_order_form.html', {
                    'product_order_form': form,
                    'product': product
                })

            # Generate unique order number
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            unique_id = str(uuid.uuid4())[:8].upper()
            order_number = f'ORD-{timestamp}-{unique_id}'

            # Get user information
            user = request.user
            customer_name = user.get_full_name() or user.username
            customer_email = user.email or 'noemail@example.com'

            # Create the Order
            order = Order.objects.create(
                user=user,
                order_number=order_number,
                customer_name=customer_name,
                customer_email=customer_email,
                is_active=True
            )

            # Create the ProductOrder
            ProductOrder.objects.create(
                order=order,
                product_name=product,
                quantity=quantity,
                price_per_item=price_per_item
            )

            # Update product stock
            product.stock -= quantity
            product.save()

            # Success message
            messages.success(
                request,
                f'Order #{order.order_number} created successfully! {quantity}x {product.name} added to your orders.'
            )

            # Redirect to My Orders
            return redirect('order_list')

        else:
            # Form is invalid - re-render with errors
            product_id = request.POST.get('product_name')
            product = None
            if product_id:
                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    pass

            return render(request, 'orders/product_order_form.html', {
                'product_order_form': form,
                'product': product
            })
    