from django.contrib import admin
from django.urls import include, path
from api import views
from api.views import *

urlpatterns = [
    path('signup/',signup.as_view()),
    path('login/',login.as_view()),
    path('get/',getproducts.as_view()),
    path('add/',addproducts.as_view()),
    path('UpdateProduct/<str:pk>',UpdateProduct.as_view()),
    path('DeleteProduct/<str:pk>',DeleteProduct.as_view()),
    path('EachProduct/<str:pk>',EachProduct.as_view()),
    path('AddToKart/',AddToKart.as_view()),
    path('UsersCart/',UsersCart.as_view()),
    path('RemoveProductFromCart/',RemoveProductsFromCart.as_view())
    
]