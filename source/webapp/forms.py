from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remains', 'price', 'image')
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'category': 'Категория',
            'remains': 'Остаток',
            'price': 'Цена',
            'image': 'Картинка'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if True in [n.isdigit() for n in name]:
            raise ValidationError('Имя не может состоять из чисел!')
        elif len(name) < 2:
            raise ValidationError('Имя не может состоять из одного символа!')
        return name.capitalize()


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['user_name', 'phone', 'address']
        labels = {
            'user_name': 'Имя пользователя',
            'phone': 'Телефон',
            'address': 'Адрес'
        }
