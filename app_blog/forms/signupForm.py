'''
A form instance to be used in the signup page
'''
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='', max_length=32)
    password = forms.CharField(max_length=32)
    verify_password = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=32)

    # add custom form validation
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')
        # check if username is available
        if User.objects.filter(username=username).exists():
            self.add_error('username', "username is taken!")
        if password and verify_password:
            if password != verify_password:
                self.add_error('verify_password', "password doesn't match!")
