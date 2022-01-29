from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ Views from products, query selector and pagination """
    
    products = Product.objects.all() 
    query = request.GET.get('q')

    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)





def product_page(request, product_id):
    """ Views from product especific id"""
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_id.html', context)