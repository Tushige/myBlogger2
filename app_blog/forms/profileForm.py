'''
A form instance to be used in the signin page
'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(label='', max_length=32, required=False)
    occupation = forms.CharField(label='', max_length=32, required=False)
    employment = forms.CharField(label='', max_length=32, required=False)
    biography = forms.CharField(widget=forms.Textarea, required=False)
