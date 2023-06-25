import random

from django.shortcuts import render
from .models import *


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    random_products = random.sample(list(products), 3)
    f_product = random_products[0]
    s_product = random_products[1]
    t_product = random_products[2]
    return render(request, 'home/home.html', {'f_product': f_product, 's_product': s_product, 't_product': t_product, 'category': category})


def all_products(request, id=None):
    products = Product.objects.all()
    category = Category.objects.all()
    if id:
        data = Category.objects.get(id=id)
        products = products.filter(category=data)
    return render(request, 'home/product.html', {'products': products, 'category': category})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    category = Category.objects.all()
    return render(request, 'home/detail.html', {'product': product, 'category': category})


def about(request):
    category = Category.objects.all()
    return render(request, 'home/about.html', {'category': category})


def contact(request):
    category = Category.objects.all()
    return render(request, 'home/contact.html', {'category': category})


