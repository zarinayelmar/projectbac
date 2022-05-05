from .models import Salt
from django. forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.models import User
from django. forms import CharField, ModelForm, TextInput, Textarea
from django.forms import TextInput,PasswordInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class SaltForm(ModelForm):
    class Meta:
        model = Salt
        fields = ['atu', 'malimet']

        widgets = {
           "atu": TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Салт-дәстүр'
           }),
           "malimet": Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'Салт-дәстүр туралы мәлімет'
           }),

        }

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=30, label="Логин",validators=[alphanumeric])
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    is_staff = False
    is_active=False
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','is_staff','is_active')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')

            return cd['password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))