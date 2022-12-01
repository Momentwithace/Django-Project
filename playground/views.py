from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


# Create your views here.

def say_hello(request):
    query_set = Product.objects.all()
    for obj in query_set:
        print(obj)

    return render(request, 'index.html', {
        'name': 'Ace'
    })
