from django.urls import path, include

from webapp.views.products import products_view, product_details

urlpatterns = [
    path("__debug__/", include('debug_toolbar.urls')),
    path("", products_view, name="products_view"),
    path("product/<int:pk>", product_details, name="product_details")
]
