from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product


# Create your views here.

def say_hello(request):
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(price__lt=20))
    return render(request, 'index.html', {
        'name': 'Ace', 'products': list(queryset)
    })
