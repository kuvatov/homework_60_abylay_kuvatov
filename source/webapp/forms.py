from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remains', 'price')
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'category': 'Категория',
            'remains': 'Остаток',
            'price': 'Цена'
        }
