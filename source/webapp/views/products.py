from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Product, CategoryChoice


# Create your views here.
def products_view(request: WSGIRequest):
    context = {
        'products': Product.objects.all(),
        'categories': CategoryChoice.choices
    }
    return render(request, 'products_view.html', context=context)
