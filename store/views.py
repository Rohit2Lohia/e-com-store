from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    # context=['shirt', 'trouser', 'sports', 'watch', 'wallet', 'earphones', 'apple', 'mango', 'banana', 'grapes', 'Tojo']
    # for idx,item in enumerate(context):
    #     context[idx]=context[idx].capitalize()
    products=Product.objects.all()
    for idx,item in enumerate(products):
        products[idx].name=products[idx].name.capitalize()
    context={ 'products':products }
    return render(request, 'store/Store.html',context)

def cart(request):
    context_to_pass={}
    return render(request, 'store/Cart.html')

def checkout(request):
    context_to_pass={}
    return render(request, 'store/Checkout.html')
