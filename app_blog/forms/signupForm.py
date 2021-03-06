'''
A form instance to be used in the signup page
'''
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='', max_length=32)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=32)
    verify_password = forms.CharField(widget=forms.PasswordInput(), max_length=32)
    email = forms.EmailField(max_length=32)

    # add custom form validation
    def clean(self):
        # retrieve user input
        cleaned_data = super(SignupForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')

        # check if username is available
        if User.objects.filter(username=username).exists():
            # add 'error' to the 'username' field
            self.add_error('username', "username is taken!")

        # check if password and 2nd entry match
        if password and verify_password:
            if password != verify_password:
                # add 'error' to the 'password' field
                self.add_error('verify_password', "passwords don't match!")
