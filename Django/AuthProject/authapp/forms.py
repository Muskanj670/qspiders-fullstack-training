from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError(f"Email {email} already exist")
        elif not email.lower().endswith("@gmail.com"):
            raise forms.ValidationError(f'Only gmail accounts are allowed....')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        length = len(username)
        if length < 5 or not username[0].isalpha():
            raise forms.ValidationError(f'Invalid Username:\n1. Username must contain 5 characters and should starts with alphabet')
        return username
    def clean_password(self):
        password = self.cleaned_data['password']
        import re
        if (
            len(password) < 8
            or not re.search(r"\d", password)
            or not re.search(r"[A-Za-z]", password)
            or not re.search(r"[^\w\s]", password)
        ):
            raise forms.ValidationError(f"Password must contain:8 Characters, Numbers, Alphabets and Special Characters ")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(f'Password do not match...')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
