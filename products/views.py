from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
from .filter import ProductFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .filter import ProductFilter


class Home(ListView):
    model = Product
    template_name = 'products/home.html'


def get_context_data(request):
    # context = super().get_context_data(**kwargs)
    filter = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'products/filter.html', {'filter': filter})


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product


# def product_list(request):
#     filter = ProductFilter(request.GET, queryset=Product.objects.all())
#     return render(request, 'products/filter.html', {'filter': filter})



