from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product
from products.filters import ProductFilter

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 3
    queryset = Product.objects.all().order_by('name')


class ProductSearchView(ListView):
    model = Product
    template_name = 'products/product_search_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


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
