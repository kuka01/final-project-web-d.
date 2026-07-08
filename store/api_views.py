from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Order, Phone, Review
from .serializers import (
    CategorySerializer,
    OrderSerializer,
    PhoneSerializer,
    ReviewSerializer,
    UserLoginSerializer,
    UserRegisterSerializer,
)

@api_view(['POST'])
def api_login(request):
    
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "username": user.username})
        return Response({"detail": "Неверное имя пользователя или пароль."}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    
    request.user.auth_token.delete()
    return Response({"detail": "Вы успешно вышли из системы."}, status=status.HTTP_200_OK)

class UserRegisterView(APIView):
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def api_category_list(request):
    
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_phone_reviews(request, pk):
    
    phone = get_object_or_404(Phone, pk=pk)
    
    if request.method == 'GET':
        reviews = phone.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(phone=phone, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhoneListAPIView(APIView):
    

    def get(self, request):
        
        phones = Phone.objects.select_related('category').all()
        
        q = request.query_params.get('q')
        category_id = request.query_params.get('category')
        sort = request.query_params.get('sort')
        
        if q:
            phones = phones.filter(name__icontains=q) | phones.filter(brand__icontains=q)
        if category_id:
            phones = phones.filter(category_id=category_id)
        if sort:
            phones = phones.order_by(sort)
            
        serializer = PhoneSerializer(phones.distinct(), many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhoneDetailAPIView(APIView):
    

    def get_object(self, pk):
        return get_object_or_404(Phone, pk=pk)

    def get(self, request, pk):
        
        phone = self.get_object(pk)
        serializer = PhoneSerializer(phone)
        return Response(serializer.data)

    def put(self, request, pk):
        
        phone = self.get_object(pk)
        serializer = PhoneSerializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        
        phone = self.get_object(pk)
        serializer = PhoneSerializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        phone = self.get_object(pk)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_phone_list_readonly(request):
    phones = Phone.objects.select_related('category').all()

    q = request.query_params.get('q')
    category_id = request.query_params.get('category')
    sort = request.query_params.get('sort')

    if q:
        phones = phones.filter(name__icontains=q) | phones.filter(brand__icontains=q)
    if category_id:
        phones = phones.filter(category_id=category_id)
    if sort:
        phones = phones.order_by(sort)

    serializer = PhoneSerializer(phones.distinct(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_phone_detail_readonly(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    serializer = PhoneSerializer(phone)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_category_detail(request, pk):
    
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewListCreateAPIView(APIView):
    

    def get(self, request):
        
        reviews = Review.objects.select_related('user', 'phone').all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(user=request.user)
            else:
                return Response(
                    {"detail": "Для создания отзыва необходима авторизация."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_review_detail(request, pk):
    
    review = get_object_or_404(Review, pk=pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListCreateAPIView(APIView):
    

    def get(self, request):
        
        orders = Order.objects.select_related('phone', 'user').all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(user=request.user)
            else:
                return Response(
                    {"detail": "Для создания заказа необходима авторизация."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_order_detail(request, pk):
    
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

