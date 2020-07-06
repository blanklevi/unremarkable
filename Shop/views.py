from django.shortcuts import render, redirect
from .models import *
from Users.models import *

def index(request):
    # User info
    if request.session['log_email'] == []:
        logged_user = []
        sign_in_button = ["Levi is the best"]
    else:
        logged_user = request.session['log_email']
        sign_in_button = [] 
    
    # Shop info
    products = Product.objects.all()

    context = {
        'logged_user': logged_user,
        'sign_in_button': sign_in_button,
        'products': products,
    }
    return render(request, "Shop/index.html", context)

def cart_page(request):
    # This is a ratchet workaround for "is someone logged in?"
    if request.session['log_email'] == []:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
        }
    else:
        logged_user = request.session['log_email']
        user = User.objects.filter(email=logged_user)
        for u in user:
            customer = u.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    context = {
        'items': items,
        'order': order,
    }
    return render(request, "Shop/cart.html", context)

def checkout_page(request):
    # This is a ratchet workaround for "is someone logged in?"
    if request.session['log_email'] == []:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
        }
    else:
        logged_user = request.session['log_email']
        user = User.objects.filter(email=logged_user)
        for u in user:
            customer = u.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    context = {
        'items': items,
        'order': order,
    }
    return render(request, "Shop/checkout.html", context)
