from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


# Create your views here.

def say_hello(request):
    product = Product.objects.order_by('price')[0]
    product = Product.objects.earliest()
    product = Product.objects.latest()
    return render(request, 'index.html', {
        'name': 'Ace', 'product': product
    })
