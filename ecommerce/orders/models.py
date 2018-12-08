from django.db import models
from datetime import datetime, timedelta
from accounts.models import MyUser
from products.models import Product

# Create your models here.


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username

    def get_order_items(self):
        return self.items.all()

    def get_order_total(self):
        return sum([item.product.price for item in self.items.all()])
