from django.shortcuts import render
from Store.models import Product


def Home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
