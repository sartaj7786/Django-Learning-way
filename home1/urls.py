from django.contrib import admin
from django.urls import path
from home1 import views

urlpatterns = [

    path('',views.index, name='home1'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact')
]
