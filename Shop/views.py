from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from Users.models import *
import json
import datetime

def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    # Shop info
    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems,
    }
    return render(request, "Shop/index.html", context)

def cart_page(request):
    # Easier way to do the "Is a user logged in?"
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, "Shop/cart.html", context)

def checkout_page(request):
    # Easier way for "is someone logged in?"
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, "Shop/checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    # Easier way to do user authentication
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        # Protect from hax
        if total == float(order.get_cart_total):
            order.complete = True
        order.save()
        
        # If it is not a digital product
        if order.shipping == True:
            ShippingAddress.objects.create(customer=customer, order=order, address=data['shipping']['address'], city=data['shipping']['city'], state=data['shipping']['state'], zipcode=data['shipping']['zipcode'])
    else:
        print("User is not logged in currently")

    return JsonResponse('Payment Completed', safe=False)
