from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/products/list/'


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products/product_update.html'
    success_url = '/products/list/'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = '/products/list/'
