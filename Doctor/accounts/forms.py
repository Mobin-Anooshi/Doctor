from django import forms
from accounts.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField




class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('user_name','full_name','phone_number')
        
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you cant change this password<a href=\"../password/\">This form</a>')
    class Meta:
        model = User
        fields = ('user_name','phone_number','full_name','last_login')