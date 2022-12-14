from django.db.models.functions import Concat
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value
from django.db.models.aggregates import Avg, Sum, Count, Max, Min
from django.contrib.contenttypes.models import ContentType

from store.models import Product, OrderItem, Customer, Collection, Order
from tags.models import TaggedItem


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


def aggregate(request):
    result = Product.objects.aggregate(count=Count('id'), min_price=Min('price'))
    return render(request, 'aggregate.html', {
        'name': 'Aggregate for computing calculation',
        'result': result
    })


def annotation(request):
    queryset = Customer.objects.annotate(is_new=Value(True))
    return render(request, 'annotate.html', {
        'name': 'Annotation', 'result': list(queryset)
    })


def func(request):
    queryset = Customer.objects.annotate(
        full_name=Concat('firstname', Value(''), 'lastname')
    )
    return render(request, 'func.html', {
        'name': 'Func methods', 'result': list(queryset)
    })


def grouping(request):
    queryset = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, 'grouping.html', {
        'name': 'Grouping methods', 'result': list(queryset)
    })


def contentType(request):
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
        content_Type=content_type,
        object_id=1
    )

    return render(request, 'content.html', {
        'name': 'Content Types Usage', 'tags': list(queryset)
    })


def record(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()

    return render(request, 'record.html', {
        'name': 'Content Types Usage', 'new_record': collection
    })


def update(request):
    collection = Collection.objects.get(pk=11)
    collection.title = 'Games'
    collection.featured_product = None
    collection.save()

    # another way to update a record is

    Collection.objects.filter(pk=11).update(featured_product=None)


def delete(request):
    collection = Collection.objects.get(pk=11)
    collection.delete()

    Collection.objects.filter(id_gt=5).delete()


def transaction(request):
    order = Order()
