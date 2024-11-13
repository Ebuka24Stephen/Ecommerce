from django.db import models
from django.contrib.auth.models import User 
from shop.models import Product
class Order(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', related_name='order_items',on_delete=models.CASCADE )
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity
