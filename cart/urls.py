from django.urls import path 
from .views import *

urlpatterns = [
    path('details/<int:cart_id>/', cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', cart_add, name='cart_add'),
    path('cart-remove/<int:product_id>/', cart_remove, name='cart_remove')
]
