'''
A form instance to be used in the signin page
'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms

class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                              'placeholder': 'your username'
                              }), label='', max_length=32)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
                               'placeholder':'your password'
                               }), max_length=32)
