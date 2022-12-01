from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.

def say_hello(request):
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:

        return render(request, 'index.html', {
            'name': 'Ace'
        })
