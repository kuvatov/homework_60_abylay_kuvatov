from django import forms
from django.core.exceptions import ValidationError

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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if True in [n.isdigit() for n in name]:
            raise ValidationError('Имя не может состоять из чисел!')
        elif len(name) < 2:
            raise ValidationError('Имя не может состоять из одного символа!')
        return name.capitalize()
