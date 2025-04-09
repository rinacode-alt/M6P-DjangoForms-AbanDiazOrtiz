from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Supplier, WaterBottle
def home(request):
    return render(request, 'MyInventoryApp/base.html')


def view_suppliers(request):
    suppliers = Supplier.objects.all() 
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers': suppliers})


def view_bottles(request):
    bottles = WaterBottle.objects.all()  
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles': bottles})

def add_bottle(request):
    return render(request, 'MyInventoryApp/add_bottle.html')

