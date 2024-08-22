from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager,PermissionsMixin
from django.utils import timezone

class CustomUserManger(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("please insert your email")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email=None , password=None , **extra_fields) :
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    def create_superuser(self,email=None , password=None , **extra_fields) :
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email,password,**extra_fields)
    
class User(AbstractUser,PermissionsMixin):
    ROLE = [
        ('Admin', 'Admin'),
        ('MEMBER', 'MEMBER'),
        ('LIBRARY', 'LIBRARY'),
    ]
    role = models.CharField(max_length=24, choices=ROLE, default='MEMBER')
    email=models.EmailField(blank=True,unique=True,default='')
    name=models.CharField(max_length=255,blank=True,default='')

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    datajoined=models.DateTimeField(default=timezone.now)
    objects=CustomUserManger()
    USERNAME_FIELD="email"
    EMAIL_FIELD="email"
    REQUIRED_FIELDS=[]
    