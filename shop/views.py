from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category


def product_list(request,category_slug=None):
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(categories, slug=category_slug)
        products = Product.objects.filter(available=True, category=category)
    else:
        products = Product.objects.filter(available=True)
        category = None
    return render(request, 'shop/product_list.html', {'category':category, 'categories':categories, 'products':products})

def product_detail(request,id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/product_detail.html', {'product':product})