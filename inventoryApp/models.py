from django.db import models
from datetime import date

# Models for products

class Product(models.Model):
    name = models.CharField(max_length=350)
    type = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100, null=True, blank=True)

  

class Stock(models.Model):
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    

# Models about users

class User(models.Model):
    name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=254)
    pswd = models.CharField(max_length=15, null=True)
    date = models.DateField(null=True, blank=True)

  
# Models about selling products

class Invoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date = models.DateField(default=date.today)

  