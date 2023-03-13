from django.db.models import Q
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product, CategoryChoice


# Create your views here.
class ProductsView(ListView):
    model = Product
    template_name = 'product/products_view.html'
    context_object_name = 'products'
    ordering = ['category', 'name']
    paginate_by = 6
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value().capitalize()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)

        if self.search_value:
            query = Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product/product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = CategoryChoice.choices
        context['categories'] = categories
        return context


class ProductAddView(CreateView):
    model = Product
    template_name = 'product/product_add.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk': self.object.pk})


class ProductEditView(UpdateView):
    model = Product
    template_name = 'product/product_edit.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product

    def get(self, request, *args, **kwargs):
        return self.delete(request)

    def get_success_url(self):
        return reverse('home')
