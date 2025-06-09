from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        help_texts = {'username': ''}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ['user']
