from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from datetime import date
from .helpers import *
import datetime



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
    def create(self, data):
        user = User.objects.create(
            email=data.get('email'),
            password = data.get('password'),
            username=data.get('username'),
            )
        user.set_password(data.get('password'))
        user.save()
        return user
    def validate(seld,data):
        user_email = User.objects.filter(email=data.get('email')).exists()
        if user_email:
            raise serializers.ValidationError({'error':'Email Already Exists Try With Another'})
        else:
            return data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    def create(self,data):
        product = Product.objects.create(user = data.get('user'),title = data.get('title'),desc = data.get('desc'),image = data.get('image'),datestamp = getdate(),timestamp = gettime())
        product.save()
        return product
    
