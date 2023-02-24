from django.contrib import admin

from webapp.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'category', 'remains', 'price', 'is_deleted', 'created_at',
                    'updated_at', 'deleted_at']
    list_filter = ['name', 'category', 'remains', 'price', 'created_at']
    search_fields = ['name', 'category', 'price']
    fields = ['name', 'description', 'image', 'category', 'remains', 'price', 'created_at']
    list_editable = ['name', 'description', 'image', 'category', 'remains', 'price', 'is_deleted']
    readonly_fields = ['created_at', 'updated_at', 'deleted_at']


admin.site.register(Product, ProductAdmin)
