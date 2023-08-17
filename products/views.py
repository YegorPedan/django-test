from django.shortcuts import render

from products.models import Product
""" That's in not funtion
it's a controllers """


def index(request):
    context = {
        'title': 'Hallo, Eliot',
        'store_name': 'luxury store',
        'is_exists': True,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'store_name': 'Store - магазин',
        'products': Product.objects.all(),
        'categories': Product.objects.all()
    }
    return render(request, 'products/products.html', context)
