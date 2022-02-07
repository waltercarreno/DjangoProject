from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bag.models import ShopCart, ShopCartForm
from products.models import Category, Product



def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    checkproduct = ShopCart.objects.filter(product_id=id)
    if checkproduct:
        control = 1
    else:
        control = 0
    
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data[ 'quantity']
                data.save()
            else:
                data = ShopCart()  # model ile bağlantı kur
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = 1
                data.save() 
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    #return HttpResponse(str(total))
    context={'shopcart': shopcart,
             'category':category,
             'total': total,
             }
    return render(request,'bag/bag.html',context)