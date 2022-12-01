from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


# Create your views here.

def say_hello(request):
    queryset = Product.objects.filter(inventory=F('price'))
    return render(request, 'index.html', {
        'name': 'Ace', 'products': list(queryset)
    })
