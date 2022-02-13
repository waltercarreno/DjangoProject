from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for id, quantity in bag.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'id': id,
            'quantity': quantity,
            'product': product,
        })

    if total > 50:
        delivery = 0
    else:
        delivery = 5        
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context