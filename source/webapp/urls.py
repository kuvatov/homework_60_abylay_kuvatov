from django.urls import path, include

from webapp.views.carts import add_to_cart, cart, remove_from_cart
from webapp.views.orders import create_order
from webapp.views.products import ProductsView, ProductDetailsView, ProductAddView, ProductEditView, ProductDeleteView

urlpatterns = [
    path("__debug__/", include('debug_toolbar.urls')),
    path("", ProductsView.as_view(), name="home"),
    path("products", ProductsView.as_view(), name="products_view"),
    path("product/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
    path("product/add", ProductAddView.as_view(), name="product_add"),
    path("product/<int:pk>/edit", ProductEditView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("cart/add/<int:pk>", add_to_cart, name='add_to_cart'),
    path("cart", cart, name='cart_view'),
    path("cart/delete/<int:pk>", remove_from_cart, name='remove_from_cart'),
    path("order/add", create_order, name='create_order')
]
