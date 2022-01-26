from django.shortcuts import render

# Create your views here.


def index(request):
    """ idex home """

    return render(request, 'home/index.html')