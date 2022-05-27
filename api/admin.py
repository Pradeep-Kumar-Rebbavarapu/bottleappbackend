from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','image']
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','quantity','Total_Price']