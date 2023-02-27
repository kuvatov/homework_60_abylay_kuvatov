from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from webapp.models import Product, CategoryChoice


# Create your views here.
def products_view(request: WSGIRequest):
    context = {
        'products': Product.objects.exclude(is_deleted=True).order_by('category', 'name'),
        'categories': CategoryChoice.choices
    }
    return render(request, 'products_view.html', context=context)


def product_details(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', context={
        'product': product,
        'categories': CategoryChoice.choices
    })
