from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    products= Product.objects.all()
    print(products)
    num = len(products)
    number_slides=num//4 + ceil((num/4)-(num//4))
    params= {'no_of_slides':number_slides,'range':range(1,number_slides),'product':products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("CONTACT")

def tracker(request):
    return HttpResponse("TRACKER")

def search(request):
    return HttpResponse("SEARCH")

def productView(request):
    return HttpResponse("PRODUCTVIEW")

def checkout(request):
    return HttpResponse("CHECKOUT")