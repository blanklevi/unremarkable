from django.urls import path
from . import views
from Marketing.views import email_list_signup

urlpatterns = [
    # path('about', views.about_page, name="about"),
    # path('subscribe', email_list_signup, name="subscribe"),
]
