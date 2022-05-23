from django.contrib import admin
from django.urls import include, path
from api import views
from api.views import *

urlpatterns = [
    path('signup/',signup.as_view()),
    path('login/',login.as_view()),
    path('getadd/',getaddproducts.as_view()),
    path('rud/<pk>/',rudproducts.as_view()),
    
]