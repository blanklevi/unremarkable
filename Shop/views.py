from django.shortcuts import render, redirect

def index(request):
    context = {}
    return render(request, "Shop/index.html", context)

def cart_page(request):
    context = {}
    return render(request, "Shop/cart.html", context)

def checkout_page(request):
    context = {}
    return render(request, "Shop/checkout.html", context)
