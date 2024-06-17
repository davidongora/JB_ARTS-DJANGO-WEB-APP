from django.shortcuts import render
from .models import Products, Bottles, Gallery

# Create your views here.


def home(request):
    products = Products.objects.all()
    bottle = Bottles.objects.all()  
    gall = Gallery.objects.all()
    return render(request, 'index.html', {'products': products, 'bottle': bottle, 'gall': gall})


