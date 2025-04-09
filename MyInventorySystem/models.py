from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def __str__(self):
        return self.username

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def getName(self):
        return self.name
        
    def getContactInfo(self):
        return self.contact_info
        
    def getLocation(self):
        return self.location
    
    def __str__(self):
        return self.name