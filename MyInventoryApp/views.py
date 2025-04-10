from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Supplier, WaterBottle, Account


id = 0

def login_view(request):
    global id
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            account = Account.objects.get(username=username)
            if account.getPassword() == password:
                request.session['user_id'] = account.id
                request.session['username'] = account.username
                id = account.pk
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

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'username' in request.session:
        del request.session['username']
    
    return redirect('login')

def view_supplier(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    account = get_object_or_404(Account, pk=id)
    suppliers = Supplier.objects.all()
    return render(request, 'MyInventoryApp/suppliers.html', {'suppliers': suppliers, 'account': account})

def view_bottles(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    account = get_object_or_404(Account, pk=id)
    bottles = WaterBottle.objects.all()
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles': bottles, 'account': account})

def view_bottle_details(request, pk):
    if 'user_id' not in request.session:
        return redirect('login')
    
    account = get_object_or_404(Account, pk=id)
    bottle = get_object_or_404(WaterBottle, pk=pk)
    return render(request, 'MyInventoryApp/view_bottle_details.html', {'bottle': bottle, 'account': account})

def delete_bottle(request, pk2):
    if 'user_id' not in request.session or request.session['user_id'] != id:
        return redirect('login')
    
    try:
        bottle = WaterBottle.objects.get(pk=pk2)
        bottle.delete()
        return redirect('view_bottles')
    except WaterBottle.DoesNotExist:
        return redirect('view_bottles')

def add_bottle(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    account = get_object_or_404(Account, pk=id)
    suppliers = Supplier.objects.all()
    
    if(request.method == "POST"):
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouth_size = request.POST.get('mouth_size')
        color = request.POST.get('color')
        supplier = request.POST.get('supplier')
        quantity = request.POST.get('quantity')
        WaterBottle.objects.create(SKU=sku, brand=brand, cost=cost, size=size, mouthSize=mouth_size, color=color, supplier=Supplier.objects.filter(pk=supplier).first(), quantity=quantity)
        return redirect('view_supplier')
    else:
        return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers': suppliers, 'account': account})

def manage_account(request, pk):
    if 'user_id' not in request.session or request.session['user_id'] != pk:
        return redirect('login')
    
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return redirect('login')
    
    return render(request, 'MyInventoryApp/manage_account.html', {'account': account})

def change_password(request, pk):
    if 'user_id' not in request.session or request.session['user_id'] != pk:
        return redirect('login')
    
    account = Account.objects.get(pk=pk)
    
    if request.method == 'POST':
        current = request.POST.get('current_password')
        new1 = request.POST.get('new_password')
        new2 = request.POST.get('confirm_password')
        
        if current != account.getPassword():
            messages.error(request, 'Current password is incorrect.')
        elif new1 != new2:
            messages.error(request, 'New passwords do not match.')
        else:
            account.password = new1
            account.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('manage_account', pk=pk)
    
    return render(request, 'MyInventoryApp/change_password.html', {'account': account})

def delete_account(request, pk):
    if 'user_id' not in request.session or request.session['user_id'] != pk:
        return redirect('login')
    
    try:
        account = Account.objects.get(pk=pk)
        account.delete()
        request.session.flush()  # clears the session
        return redirect('login')
    except Account.DoesNotExist:
        return redirect('login')
