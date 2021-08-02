from django import forms
from .models import CustomUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control', 'id':'username'
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class':'form-control', 'id': 'email'
    }))
    contact_no = forms.IntegerField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control', 'id':'contact_no'
    }))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password1'}))
    
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'password2'}))

    class Meta:
        model = CustomUser

        fields=['username', 'email', 'contact_no', 'password1', 'password2']