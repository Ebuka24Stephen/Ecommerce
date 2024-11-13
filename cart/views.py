from django.shortcuts import render, redirect, get_object_or_404 
from .models import CartItem, Cart 
from shop.models import Product
from django.views.decorators.http import require_POST
from django.contrib import messages
@require_POST
def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')
    if cart_id:
        try:
            cart= Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
    else:
        cart = Cart.objects.create()
    request.session['cart_id'] = cart.id
    product = get_object_or_404(Product, id=product_id)
    if product.stock <= 0:
        messages.error(request, f"{product.name} is out of stock.")
        return redirect('cart_detail', cart_id=cart.id)
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    if not created:
        cart_item.quantity += 1
        #product.stock -= 1
    cart_item.save()
    #product.save()
    return redirect('cart_detail', cart_id=cart.id)

def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    return render(request, 'cart/cart_detail.html', {'cart':cart})    


@require_POST
def cart_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
        try:
            item = get_object_or_404(CartItem, product_id=product_id, cart=cart)
            item.delete()

            return redirect('cart_detail', cart_id=cart.id)
        except CartItem.DoesNotExist:
            messages.error(request, "Item not found in cart.")
            return redirect('cart_detail', cart_id=cart.id)
    else:
        messages.error(request, "No active cart.")
        return redirect('shop:product_list')
