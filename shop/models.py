from django.db import models
from django.urls import reverse
class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
        

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='media/', null=True, blank=True, default='no_image.png')
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    