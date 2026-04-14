from django import forms
from studentapp.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name','age','email']

class studentLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
