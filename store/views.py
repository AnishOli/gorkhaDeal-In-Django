from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .models import Customer, Order
import traceback




# Create your views here.
def home(request):
    context={}
    return render (request, 'store/Main.html',context)

def store(request):
    products =Product.objects.all()
    context = {'products':products}
    return render(request, 'store/Store.html' ,context)



#view for cart

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create()
        items = order.orderitem_set.all()
    else:
        items= []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/Cart.html' ,context)

# def cart(request):
#     try:
#         if request.user.is_authenticated:
#             try:
#                 customer = request.user.customer
#             except Customer.DoesNotExist:
#                 customer = Customer.objects.create(user=request.user, name=request.user.username)

#             order = Order.objects.filter(customer=customer, complete=False).order_by('-date_ordered').first()
#             if not order:
#                 order = Order.objects.create(customer=customer, complete=False)

#             items = order.orderitem_set.all()
#         else:
#             items = []
#             order = {'get_cart_total': 0, 'get_cart_items': 0}

#         context = {'items': items, 'order': order}
#         return render(request, 'store/Cart.html', context)

#     except Exception as e:
#         print("🛑 Traceback:\n", traceback.format_exc())
#         return HttpResponse(f"Error: {e}")
    
#view for checkout

def checkout(request):
    try:
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create()
            items = order.orderitem_set.all()
        else:
            items= []
            
            order = {'get_cart_total':0,'get_cart_items':0}
            print(order)
            
        context = {'items':items, 'order':order}
        return render(request, 'store/Checkout.html' ,context)

    except Exception as e:
        print("🛑 Traceback:\n", traceback.format_exc())
        return HttpResponse(f"Error: {e}")

# def checkout(request):
#     if request.user.is_authenticated:
#         try:
#             customer = request.user.customer
#         except Customer.DoesNotExist:
#             customer = Customer.objects.create(user=request.user, name=request.user.username)

#         order = Order.objects.filter(customer=customer, complete=False).order_by('-date_ordered').first()
#         if not order:
#             order = Order.objects.create(customer=customer, complete=False)

#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}

#     context = {'items': items, 'order': order}
#     return render(request, 'store/Checkout.html', context)
