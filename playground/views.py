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
    products = Product.objects.all()[:10]
    return render(request, 'all product.html', {
        'name': 'all products', 'results': list(products)
    })


def relatedField(request):
    queryset = Product.objects.values_list('id', 'title', 'collection__title')
    return render(request, 'querying related field.html', {
        'name': "Querying Related Field", 'result': queryset
    })


def orderItem(request):
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct())
    return render(request, 'orderItem.html', {
        'name': "Ordered Item", 'outcome': list(queryset)
    })


def fields(request):
    queryset = Product.objects.defer('description')
    return render(request, 'deferring fields.html', {
        'name': 'deferring fields', 'result': list(queryset)
    })


def productTable(request):
    queryset = Product.objects.select_related('collection').all()
    return render(request, 'related table.html', {
        'name': 'Related Table', 'result': list(queryset)
    })
