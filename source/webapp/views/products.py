from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import ProductForm
from webapp.models import Product, CategoryChoice


# Create your views here.
def products_view(request: WSGIRequest):
    search_product = request.GET.get('search_product')
    if search_product:
        products = Product.objects.filter(Q(name__icontains=search_product.capitalize()))
    else:
        products = Product.objects.exclude(is_deleted=True).order_by('category', 'name')
    context = {
        'products': products,
        'categories': CategoryChoice.choices
    }
    return render(request, 'products_view.html', context=context)


def product_details(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_details.html', context={
        'product': product,
        'categories': CategoryChoice.choices
    })


def product_add(request: WSGIRequest):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={
            'form': form
        })
    form = ProductForm(data=request.POST)
    if form.is_valid():
        Product.objects.create(**form.cleaned_data)
        return redirect('products_view')
    else:
        return render(request, 'product_add.html', context={
            'form': form
        })


def product_edit(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
        return render(request, 'product_edit.html', context={
            'form': form,
            'product': product
        })
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products_view')
    else:
        return render(request, 'product_edit.html', context={
            'form': form,
            'product': product
        })


def product_delete(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products_view')
