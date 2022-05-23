from tkinter import ttk
from django.db import models
from django.contrib.auth.models import User
from .helpers import *
# Create your models here.
def upload(instance,filename):
    return f'{instance.title}_{filename}'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_id', default=None, blank=True, null=True)
    title = models.CharField(max_length=225, null=True,
                             blank=True, default=None)
    desc = models.CharField(max_length=1000, null=True,
                            blank=True, default=None)
    image = models.FileField(upload_to=upload)
    datestamp = models.CharField(max_length=225, default=getdate,null=True,blank=True)
    timestamp = models.CharField(max_length=225, default=gettime,null=True,blank=True)