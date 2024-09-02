#Define views to handle requests and return responses in views.py:


from django.shortcuts import render
from products.models import Product

print(Product.objects.all()) 

def product_list(request): # product
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products':products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    print(product)
    return render(request, 'product_detail.html', {'product': product})



