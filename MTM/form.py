from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class KiderForm(forms.ModelForm):
    class Meta:
        model = Kider
        fields = ['vasiyni_ismi','farzand_ismi',"farzand_yoshi",'tel_nomer','joylashuv','xabar']
        

class LoginForm(forms.Form):
    UserName = forms.CharField(
        label='User Name',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs = {'placeholder':'User Name'}),
    )
    password = forms.CharField(
        label='password',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'password','type':'password'})
    )