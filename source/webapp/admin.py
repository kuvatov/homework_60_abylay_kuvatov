from django.contrib import admin

from webapp.models import Product, Cart, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'category', 'remains', 'price', 'is_deleted', 'created_at',
                    'updated_at', 'deleted_at']
    list_filter = ['name', 'category', 'remains', 'price', 'created_at']
    search_fields = ['name', 'category', 'price']
    fields = ['name', 'description', 'image', 'category', 'remains', 'price', 'created_at']
    list_editable = ['name', 'description', 'image', 'category', 'remains', 'price', 'is_deleted']
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']


class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'created_at', 'updated_at']
    list_filter = ['product', 'quantity', 'created_at']
    search_fields = ['product', 'quantity', 'created_at']
    fields = ['product', 'quantity', 'created_at']
    readonly_fields = ['created_at', 'updated_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['products', 'user_name', 'phone', 'address', 'created_at']
    list_filter = ['products', 'user_name', 'phone', 'address', 'created_at']
    search_fields = ['products', 'user_name', 'phone', 'address', 'created_at']
    fields = ['products', 'user_name', 'phone', 'address', 'created_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order)
