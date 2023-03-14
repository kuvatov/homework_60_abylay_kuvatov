from django.shortcuts import redirect, render
from webapp.models import Order, Product


def create_order(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        order = Order.objects.create(user_name=user_name, phone=phone, address=address)
        for cart_item in request.session.get('cart', []):
            product_id = cart_item['product_id']
            quantity = cart_item['quantity']
            product = Product.objects.get(pk=product_id)
            if quantity <= product.remains:
                order_product = Order(order=order, product=product, quantity=quantity)
                order_product.save()
                product.remains -= quantity
                product.save()
        request.session['cart'] = []
        return redirect('home')
    else:
        return render(request, 'create_order.html')
