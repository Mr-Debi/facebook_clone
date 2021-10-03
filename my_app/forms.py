from django import forms
from .models import *
from django.contrib.auth.models import User

class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

