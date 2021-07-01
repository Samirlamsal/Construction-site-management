from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Transaction
from django.forms import ModelForm


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'validate', 'placeholder': 'Your Username', 'style': 'width: 100%;', 'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(
        attrs={'placeholder': 'Password', 'style': 'width: 100%;', 'class': 'form-control'}))


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['confirmation_status']
