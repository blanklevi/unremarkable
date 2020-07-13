from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    # path('register_submit', views.register, name='register_submit'),
    path('login', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    # path('login_submit', views.log_in, name='login_submit'),
    path('logout', views.log_out, name='logout'),
]