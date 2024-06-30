from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Order, OrderItem, Cart
from decimal import Decimal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
        
class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(     # represents the relationship between MenuItem and Category by using the category's id
        queryset = Category.objects.all()
    )
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'category', 'price' 'featured']
        
class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(   # represents the relationship between Order and User by using the user's id
        queryset = User.objects.all(),
        default = serializers.CurrentUserDefault()  # Validation: automatically sets the user to the current user
        )
    def validate_items(self, attrs):
        attrs['price'] = attrs['quantity'] * attrs['unit_price']
        if len(attrs) == 0:
            raise serializers.ValidationError("You must add items to your cart")
        return attrs   
    
    class Meta:
        model = Cart
        fields = ['user', 'menuitem', 'unit_price', 'quantity', 'price']
        extra_kwargs = {
            'price': {'read_only': True}  # Validation: price is read-only, it is calculated based on the quantity and unit_price
        }
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order', 'menuitem', 'quantity', 'price']
        
        
class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True, read_only=True, source='order')
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'orderitem', 'total', 'status', 'delivery_crew', 'date']
        