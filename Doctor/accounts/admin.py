from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserChangeForm,UserCreationForm
from accounts.models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    readonly_fields =('last_login',)
    list_display = ('user_name','full_name','is_admin')
    list_filter = ('is_admin',)
    
    
    fieldsets = (
        (None , {'fields':('user_name','full_name','phone_number','password')}),
        ('permissions',{'fields':('is_admin','is_active','last_login')}),
    )
    add_fieldsets = (
        (None,{'fields':('phone_number','user_name','full_name','password')}),
    )
    
    ordering = ['user_name'] 
    filter_horizontal = ()
admin.site.unregister(Group)
admin.site.register(User,UserAdmin)