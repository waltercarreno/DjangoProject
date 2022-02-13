from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    
    bag = request.session.get('bag', {})

    if id in list(bag.keys()):
        bag[id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[id] = quantity
    else:
        bag.pop(id)
    
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

