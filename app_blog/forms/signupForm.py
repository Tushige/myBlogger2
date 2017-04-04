'''
A form instance to be used in the signup page
'''
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(label='', max_length=32)
    password = forms.CharField(max_length=32)
    verify_password = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=32)

    # form clean method
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')
        if password and verify_password:
            if password != verify_password:
                cleaned_data['password'] = 'hello'
                self.add_error('verify_password', "password doesn't match!")
