from itertools import product
from django.db import models
from django.contrib.auth.models import User
from .helpers import *
import uuid
# Create your models here.
def upload(instance,filename):
    return f'{instance.title}_{filename}'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None, blank=True, null=True)
    title = models.CharField(max_length=225, null=True,
                             blank=True, default=None)
    desc = models.CharField(max_length=1000, null=True,
                            blank=True, default=None)
    price = models.IntegerField(default=None,null=True,blank=True)
    image = models.FileField(upload_to=upload)
    datestamp = models.CharField(max_length=225, default=getdate,null=True,blank=True)
    timestamp = models.CharField(max_length=225, default=gettime,null=True,blank=True)

class Cart(models.Model):
    user = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE,default=None, blank=True, null=True)
    product = models.ForeignKey(Product,to_field="id",on_delete=models.CASCADE,default=None, blank=True, null=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    Total_Price = models.IntegerField(default=None,null=True,blank=True)
    product_title = models.CharField(max_length=225, null=True,
                             blank=True, default=None)
    product_image  = models.URLField(default=None)
    datestamp = models.CharField(max_length=225, default=getdate,null=True,blank=True)
    timestamp = models.CharField(max_length=225, default=gettime,null=True,blank=True)
