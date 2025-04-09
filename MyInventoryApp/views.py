from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Account, Supplier, WaterBottle

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            account = Account.objects.get(username=username)
            if account.getPassword() == password:
                request.session['user_id'] = account.id
                request.session['username'] = account.username
                return redirect('view_supplier')
            else:
                messages.error(request, 'Invalid login')
        except Account.DoesNotExist:
            messages.error(request, 'Invalid login')
    
    return render(request, 'MyInventoryApp/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if Account.objects.filter(username=username).exists():
            messages.error(request, 'Account already exists')
        else:
            Account.objects.create(username=username, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    
    return render(request, 'MyInventoryApp/signup.html')

def view_supplier(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/suppliers.html', {'suppliers': suppliers})

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    
    return redirect('login')

def view_bottles(request):
    if 'user_id' not in request.session:
        return redirect('login')
        
    bottles = WaterBottle.objects.all()  
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles': bottles})

def add_bottle(request):
    if 'user_id' not in request.session:
        return redirect('login')
        
    return render(request, 'MyInventoryApp/add_bottle.html')