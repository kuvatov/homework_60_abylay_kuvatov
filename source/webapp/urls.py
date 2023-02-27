from django.urls import path, include

from webapp.views.products import products_view, product_details, product_add, product_edit, product_delete

urlpatterns = [
    path("__debug__/", include('debug_toolbar.urls')),
    path("", products_view, name="products_view"),
    path("product/<int:pk>", product_details, name="product_details"),
    path("product/add", product_add, name="product_add"),
    path("product/<int:pk>/edit", product_edit, name="product_edit"),
    path("product/<int:pk>/delete", product_delete, name="product_delete")
]
