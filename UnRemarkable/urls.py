"""UnRemarkable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Marketing.views import email_list_signup

from Dashboard import views

urlpatterns = [
    #Add the Admin functionality
    path('admin/', admin.site.urls),

    # Add the Dashboard App to the project

    # These two paths are from a tut i used to learn the carousel pictures
    path('', views.blog_view, name='blog'),
    path('<int:id>/', views.detail_view, name='detail'),

    # About Page
    path('about', views.about_page, name="about"),

    # Add the Users app to the project
    path('users/', include('Users.urls')),

    # Add the Shop app to the project
    path('shop/', include('Shop.urls')),

    # Marketing
    path('subscribe', email_list_signup, name="subscribe"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
