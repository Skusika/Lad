from django.shortcuts import render
from .models import Product, Order


def index(request):
    return render(request, 'shopapp/index.html')


def products_list(request):
    products = Product.objects.all()
    context = {
        'title': 'Список всех товаров',
        'products': products,
    }
    return render(request, 'shopapp/products.html', context=context)


def orders_list(request):
    orders = Order.objects.all()
    context = {
        'title': 'Список заказов',
        'orders': orders,
    }
    return render(request, 'shopapp/orders.html', context=context)
