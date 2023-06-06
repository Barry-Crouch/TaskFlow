from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    # first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email is already registered !!')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username is already taken !!')
        return username
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))