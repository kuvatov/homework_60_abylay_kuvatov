from django.urls import path, include

from webapp.views.products import ProductsView, ProductDetailsView, ProductAddView, ProductEditView, ProductDeleteView

urlpatterns = [
    path("__debug__/", include('debug_toolbar.urls')),
    path("", ProductsView.as_view(), name="home"),
    path("products", ProductsView.as_view(), name="products_view"),
    path("product/<int:pk>", ProductDetailsView.as_view(), name="product_details"),
    path("product/add", ProductAddView.as_view(), name="product_add"),
    path("product/<int:pk>/edit", ProductEditView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete")
]
