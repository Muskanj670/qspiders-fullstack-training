from django import forms
from django.contrib.auth.models import User
from myapp.models import TODOModel

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class TODOForm(forms.ModelForm):
    status = forms.ChoiceField(choices=[('pending', 'Pending'), ('completed', 'Completed')])
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TODOModel
        fields = ['title', 'description', 'status', 'due_date']
