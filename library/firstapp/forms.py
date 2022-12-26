from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegistrFrom(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'name': 'input_registr_name', 'class': 'contaner__InputName input',  "placeholder": "Name"}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'name': 'input_registr_email', 'class': 'contaner__InputEmail input',  "placeholder": "Email"}
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"name": 'input_password', 'class': 'contaner__InputPassword1 input', 'placeholder': 'Password'}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"name": 'input_password', 'class': 'contaner__InputPassword2 input', 'placeholder': 'Password repeat'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Entrance(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'contaner__form_InputName input', 'placeholder': 'Name'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'contaner__form_InputPassword input', 'placeholder': 'Password'}
        )
    )

