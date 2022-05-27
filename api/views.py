import random
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import *
from .serializers import *
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework import status
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import *
# Create your views here.
import jwt
import datetime
from django.views.decorators.csrf import csrf_exempt 
import json
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

from .serializers import UserSerializer
from .helpers import *
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions
# Create your views here.
from django.middleware.csrf import get_token
class signup(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})
class login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']

        # checking for errors
        user = User.objects.filter(username=username).first()
        
        print(user)
        if user is None:
                    return Response({'error': 'invalid username or password'}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
                    return Response({'error': 'invalid username or password'},status=status.HTTP_404_NOT_FOUND)
        else:
            if email == user.email:
                    refresh = RefreshToken.for_user(user)
                    user.last_login = datetime.datetime.now()
                    user.save()
                    
                    return Response({
                        'message': 'login successfull',
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'username':user.username,
                        'last_login_date':getdate(),
                        'last_login_time':gettime(),
                        'email':user.email},
                        status=status.HTTP_200_OK)
                    
                    
            else:
                return Response({'errors':'email not matched'},status=status.HTTP_404_NOT_FOUND)

class getproducts(ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class addproducts(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class UpdateProduct(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class DeleteProduct(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class EachProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AddToKart(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        user = request.user
        data = request.data
        print('product',data.get('product'))
        serializer = CartSerializer(data=data)
        if(serializer.is_valid()):
            if user.username==data['user']:
                user_product_filter = Cart.objects.filter(product=data['product'])
                user_cart_filter = Cart.objects.filter(user=user)
                user_cart_product_filter = Cart.objects.filter(user=user).filter(product=data['product']).exists()
                if user_cart_product_filter:
                    print('old cart')
                    user_product_get = Cart.objects.filter(user=user).get(product=data['product'])
                    Product_Price = Product.objects.get(id=data['product']).price
                    New_Quantity = user_product_get.quantity + 1
                    New_Total_Price = (Product_Price)*(New_Quantity)
                    user_product_get.__dict__.update(quantity=New_Quantity,Total_Price=New_Total_Price)
                    user_product_get.save()
                    return Response('old cart',status=status.HTTP_200_OK)
                else:
                    print('new cart')
                    serializer.save()
                    return Response('newcart',status=status.HTTP_201_CREATED)
            else:
                
                return Response('unAuthorised',status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
            
class UsersCart(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user.username)


class RemoveProductsFromCart(APIView):
    
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        def post(self,request):
            
                user=request.user
                
                data = request.data
                
                print('product',data['product'])
                
                
                UsersCartItems = Cart.objects.filter(user=user).get(product=data['product'])
                product = Product.objects.get(id=data['product'])
                if UsersCartItems.quantity==1:
                        UsersCartItems.delete()
                        AllData = list(Cart.objects.filter(user=user.username).values())
                        
                        return JsonResponse(AllData,safe=False)
                        
                else:
                        NewQuantity = UsersCartItems.quantity-1
                        NewPrice = (NewQuantity)*(product.price)
                        UsersCartItems.__dict__.update(quantity=NewQuantity,Total_Price = NewPrice)
                        UsersCartItems.save()
                        AllData = list(Cart.objects.filter(user=user.username).values())
                        return JsonResponse(AllData,safe=False)
            
                    
            