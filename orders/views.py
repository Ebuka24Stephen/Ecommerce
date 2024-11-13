from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem 
from shop.models import Product
from .forms import OrderCreateForm
from cart.models import Cart, CartItem
def order_create(request):
    cart = None
    cart_id = request.session.get('cart_id')
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
        if not cart.items.exists():
            return redirect('cart_detail')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity = item.quantity
                )
            cart.delete()
            del request.session['cart_id']
            return redirect('order_created', order.id)
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})

def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_created.html', {'order': order})
    
            
                
            

