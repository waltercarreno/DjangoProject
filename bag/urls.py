from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopcart, name='shopcart'),
    path('addtoshopcart/<int:id>/', views.addtoshopcart, name='addtoshopcart'),
]
