from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context={}
    return render (request, 'store/Main.html',context)

def store(request):
    context = {}
    return render(request, 'store/Store.html' ,context)



#view for cart

def cart(request):
    context = {}
    return render(request, 'store/Cart.html' ,context)

#view for checkout
def checkout(request):
    context = {}
    return render(request, 'store/Checkout.html' ,context)