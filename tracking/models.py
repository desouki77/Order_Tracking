from django.db import models

# Create your models here.

class Order(models.Model):
    ORDER_STATUSES = [
        ('requested', 'Requested'),
        ('preparing', 'Preparing'),
        ('delivering', 'Delivering'),
        ('delivered', 'Delivered'),
    ]

    orderId = models.CharField(max_length=100, unique=True)
    orderName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=ORDER_STATUSES)


def __str__(self):
    return self.orderName