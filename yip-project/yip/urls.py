"""yip URL Configuration

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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('media/', views.media, name='media'),
    path('msg_from_org/', views.msg_from_org, name='msg_from_org'),
    path('prev_yip/', views.prev_yip, name='prev_yip'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('themes/', views.themes, name='themes'),
    path('why_yip/', views.why_yip, name='why_yip'),
    path('winners/', views.winners, name='winners'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]
