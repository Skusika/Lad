from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('products', views.products_list),
    path('orders', views.orders_list),
]