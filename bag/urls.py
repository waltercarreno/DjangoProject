from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path('', views.view_bag, name='view_bag'),
 path('add/<id>/', views.add_to_bag, name='add_to_bag'),
 path('adjust/<id>/', views.adjust_cart, name='adjust_cart'),
 path('remove/<id>/', views.remove_from_bag, name='remove_from_bag'),
]
