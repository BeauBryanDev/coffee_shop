from django.urls import path
from .views import  MYOrderslist , OrderDetail

urlpatterns = [
    
    path('', MYOrderslist.as_view(), name='order_list'),
    path('<int:pk>/', OrderDetail.as_view(), name='order_details'),
]
