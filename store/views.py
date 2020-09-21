from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product


# Create your views here.
def index(request):
    products = Product.get_all_products();

    return render(request , 'index.html' , {'products' : products})


def shop(request):
    products = Product.get_all_products();

    return render(request , 'shop.html' , {'products' : products})

def cart(request):
    return render(request , 'cart.html')

def about(request):
    return render(request, 'about.html')