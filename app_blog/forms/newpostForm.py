'''
A form instance to be used in the newpost page
'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms

class NewpostForm(forms.Form):
    blog_title = forms.CharField(max_length=64)
    blog_abstract = forms.CharField(widget=forms.Textarea(attrs={
                                    'cols': 10, 'rows': 5,
                                    'placeholder': 'your blog summary'
                                    }), max_length=128)
    blog_content = forms.CharField(widget=forms.Textarea, max_length=500)
