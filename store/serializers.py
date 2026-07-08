from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Order, Phone, Review

class UserLoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

class UserRegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6, write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Пароли должны совпадать."})
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username": "Пользователь с таким именем уже существует."})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Этот email уже зарегистрирован."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name']

class PhoneSerializer(serializers.ModelSerializer):
    
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Phone
        fields = [
            'id', 
            'name', 
            'brand', 
            'price', 
            'description', 
            'image_url', 
            'category', 
            'category_name', 
            'in_stock', 
            'created_at'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'phone', 'username', 'text', 'rating', 'created_at']
        read_only_fields = ['phone']

class OrderSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username', read_only=True)
    phone_name = serializers.CharField(source='phone.name', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'username', 'phone', 'phone_name', 'quantity', 'created_at']

