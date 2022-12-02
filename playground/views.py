from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, OrderItem


# Create your views here.

def say_hello(request):
    queryset = Product.objects.filter(
        Q(inventory__lt=10), Q(price__lt=20))
    return render(request, 'index.html', {
        'name': 'Ace', 'products': queryset
    })


def hi(request):
    query_set = Product.objects.order_by("title")
    return render(request, 'hi.html', {
        'name': 'Order_by', 'product': list(query_set)
    })


def productList(request):
    products = Product.objects.order_by("price")
    return render(request, 'all product.html', {
        'name': 'all product', 'result': products
    })
