from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_page, name='register_page'),
    path('register_submit', views.register, name='register_submit'),
    path('login', views.login_page, name='login_page'),
    path('login_submit', views.log_in, name='login_submit'),
    path('logout', views.log_out, name='logout'),
]