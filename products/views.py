from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product


def all_products(request):
    """ Views from products, query selector and pagination """
    
    products = Product.objects.all() 
    paginator = Paginator(products, 1)
    number_page = request.GET.get('page')
    obj_page = paginator.get_page(number_page)

    context = {
        'products': obj_page,
    }
    
    return render(request, 'products/products.html', context)


def product_page(request, product_id):
    """ Views from product especific id"""
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_id.html', context)