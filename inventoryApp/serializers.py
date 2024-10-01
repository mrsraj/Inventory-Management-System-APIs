from rest_framework import serializers
from .models import Product, Stock,User,Invoice

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['quantity']

class ProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer(source='stock_set', many=True, read_only=True)  
    class Meta:
        model = Product
        fields = ['name', 'type', 'price', 'brand', 'stock']
        
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'mobile_number', 'email', 'date']
        

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','user','product','quantity', 'total_price', 'date']
        
        