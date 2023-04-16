from django import forms
from .models import *
from django.core.exceptions import ValidationError
import hashlib



class LoginFrom(forms.Form):
    # class Meta:
    #     model = MyUsers
    #     fields = [ 'Login', 'password' ]

    Login = forms.CharField(
        max_length=255,
        label='логин'
    )
    password = forms.CharField(
        max_length=255,
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'введите пароль',
                'class': 'form-conrol cluwn'
            }
        )
    )

class RegForm(forms.ModelForm):
    def clean(self):
        pass2 = self.cleaned_data['password1']
        pass1 = self.cleaned_data['password']
        if pass2 != pass1:
            raise ValidationError("пароли не совпадают 💢")

    class Meta:
        model = MyUsers
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

class ShadowLoginForm(forms.Form):

    def check_access(self):
        login = self.cleaned_data['Login']
        passwd = hashlib.sha256(bytes(self.cleaned_data['password'], 'utf-8')).hexdigest()
        User_count = MyUsers.objects.filter(Login=login, password=passwd)
        if len(User_count) > 0:
            return User_count[0]

        else:
            raise ValidationError("вы не вошли в аккаунт 💢")

    password = forms.CharField(
        max_length=255,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form',
                'hidden' : 'True'
            }
        )
    )

    Login = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form',
                'hidden' : 'True'
            }
        )
    )

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ['Title', 'Text', 'CategoryID']

    Text = forms.CharField(
        widget=forms.Textarea,
        max_length=10000,
        label=''
    )


class commentform(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['CommentText']

    CommentText = forms.CharField(
        widget=forms.Textarea,
        max_length=10000,
        label=''
    )