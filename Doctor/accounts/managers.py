from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self,user_name,full_name,phone_number,password):
        if not user_name :
            raise ValueError('user must have phone number')
        if not full_name :
            raise ValueError('user must have email')
        if not phone_number :
            raise ValueError('user must have full name')
        
        user = self.model(user_name=user_name,full_name=full_name,phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,user_name,full_name,phone_number,password):
        user = self.create_user(user_name,full_name,phone_number,password)
        user.is_admin = True
        user.save(using=self._db)
        return user
        