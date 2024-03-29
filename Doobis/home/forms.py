from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username',  'email', 'password','account_type')


class LoginForm(forms.Form):
    username_or_phone = forms.CharField(label="Username or Phone Number")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

