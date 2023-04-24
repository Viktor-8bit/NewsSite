from django import forms
from .models import *
from django.core.exceptions import ValidationError
import hashlib

class LoginFrom(forms.Form):

    def __init__(self, *args, **kwargs):
        super(LoginFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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
                'class': 'form-control'
            }
        )
    )

class RegForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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
                'class' : 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        max_length = 255,
        label = 'Повторите пароль',
        widget = forms.PasswordInput (
            attrs = {
                'placeholder' : 'повторите пароль',
                'class' : 'form-control'
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