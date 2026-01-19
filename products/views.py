from django.shortcuts import render
from django.http import HttpResponse
from .models import Product 

# products view
def products(request):
    # 1. Grab the data
    all_bottles = Product.objects.all() 
    
    # 2. Put EVERYTHING you want to send to the page in ONE dictionary
    context = {
        'bottles': all_bottles,
        'title': 'Our Products'
    }
    
    # 3. Pass that one dictionary (context) to the template
    return render(request, 'products/products.html', context)


# about view
def about(request):
    return render(request, 'products/about.html', {'title': 'About Us'})





