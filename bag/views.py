from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def bag(request):

    return render(request, 'bag/bag.html')


def add_to_bag(request, id):
    quantity = int(request.POST.get('quantity'))
    return HttpResponse(str(quantity))