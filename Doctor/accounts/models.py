from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager
# Create your models here.




class User(AbstractBaseUser):
    user_name = models.CharField(max_length=255,unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['full_name','phone_number']
    
    objects = UserManager()
     
    def __str__(self):
        return f'{self.full_name} -{self.phone_number} '
    
    def has_perm(self , perm,obj=None):
        return  True
    
    def has_module_perms(self,app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    