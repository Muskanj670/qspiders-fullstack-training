from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", 'email', 'phno', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=50, widget= forms.PasswordInput)
