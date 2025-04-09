from django.db import models
from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    contact_info = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def getName(self):
        return self.name
        
    def getContactInfo(self):
        return self.contact_info
        
    def getLocation(self):
        return self.location
   
    def __str__(self):
        return "{} - {}, {} created at: {}".format(self.name, self.city, self.country, self.created_at)

class WaterBottle(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=100)
    mouthSize = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    suppliers = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    currentQuantity = models.IntegerField()

    def __str__(self):
        return f"SKU: {self.sku}, Brand: {self.brand}, Mouth Size: {self.mouthSize}, " \
            f"Size: {self.size}, Color: {self.color}, Supplied by: {self.suppliers.name}, " \
            f"Cost: {self.cost}, Quantity: {self.currentQuantity}"

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def __str__(self):
        return self.username