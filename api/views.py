from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import *
from .serializers import *
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
# Create your views here.
class signup(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

class getaddproducts(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class rudproducts(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
