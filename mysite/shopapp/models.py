from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    date_ordered = models.DateTimeField(auto_now=True)
    return_goods = models.BooleanField()

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.ManyToManyField(Product)

    def __str__(self):
        return self.order_name
