from rest_framework import serializers
from .models import UserProfile, Category, Product, Order, OrderItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'avatar']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'price', 'quantity', 'created_at', 'updated_at']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'item_price']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'created_at']