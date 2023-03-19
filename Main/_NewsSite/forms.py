from django import forms
from .models import *
from django.core.exceptions import ValidationError



class LoginFrom(forms.ModelForm):
    class Meta:
        model = Users
        fields = [ 'Login', 'password' ]

    password = forms.CharField(
        max_length=255,
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'введите пароль',
                'class': 'form-conrol'
            }
        )
    )

class RegForm(forms.ModelForm):

    # def clean(self):
    #    pass2 = self.cleaned_data['password1']
    #    pass1 = self.cleaned_data['password']
    #    if pass2 != pass1:
    #        raise ValidationError( {'password': "Пароли не совпадают!"})

    class Meta:
        model = Users
        fields = [ 'Login', 'email', 'password' ]

    password = forms.CharField(
        max_length = 255,
        label = 'Введите пароль',
        widget = forms.PasswordInput (
            attrs = {
                'placeholder' : 'введите пароль',
                'class' : 'form'
            }
        )
    )

    password1 = forms.CharField(
        max_length = 255,
        label = 'Повторите пароль',
        widget = forms.PasswordInput (
            attrs = {
                'placeholder' : 'повторите пароль',
                'class' : 'form'
            }
        )
    )
