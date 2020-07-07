from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shop"),
    path('cart', views.cart_page, name="cart"),
    path('checkout', views.checkout_page, name="checkout"),
    path('update_item', views.updateItem, name="update_item"),
    path('process_order', views.processOrder, name="process_order"),
]