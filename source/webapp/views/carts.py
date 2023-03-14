from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import OrderForm
from webapp.models import Product, Cart


def add_to_cart(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get('quantity', 0))
    if product.remains <= quantity:
        return redirect(request.META.get('HTTP_REFERER'))
    cart_item, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += quantity
        if cart_item.quantity > product.remains:
            cart_item.quantity = product.remains
        cart_item.save()
    else:
        cart_item.quantity = quantity
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def cart(request: WSGIRequest):
    cart_items = Cart.objects.all()
    order_form = OrderForm()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_view.html', context={
        'cart_items': cart_items,
        'order_form': order_form,
        'total': total
    })


def remove_from_cart(request: WSGIRequest, pk: int):
    cart_item = get_object_or_404(Cart, pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
