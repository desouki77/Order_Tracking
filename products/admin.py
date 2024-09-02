#To manage your products app through the Django admin interface, register your models in admin.py:

from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)