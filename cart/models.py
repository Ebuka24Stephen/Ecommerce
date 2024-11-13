from django.db import models 
from django.contrib.auth.models import User
from shop.models import Product
class Cart(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_item')
    quantity = models.IntegerField(default=1) 
    def get_total_price(self):
        return self.product.price * self.quantity