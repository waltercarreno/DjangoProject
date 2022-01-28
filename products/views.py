from django.shortcuts import render
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
