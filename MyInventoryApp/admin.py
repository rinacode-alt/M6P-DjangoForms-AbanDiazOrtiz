from django.contrib import admin
from .models import Account, Supplier, WaterBottle

# Register your models here.
admin.site.register(Account)
admin.site.register(Supplier)
admin.site.register(WaterBottle)