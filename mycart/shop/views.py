from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("ABOUT")

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