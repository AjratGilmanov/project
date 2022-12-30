from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Book

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


class Application(forms.ModelForm):
    date_of_create = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'book_author':forms.Select(attrs={'class':'select_custom'}),
        }


class Form_zakaz(forms.Form):
    CHOICE_BOOK = [(i.id, i.book_name) for i in Book.objects.all()]
    name_book = forms.ChoiceField(choices=CHOICE_BOOK, label='Books', widget=forms.Select(attrs={'class':'select_custom'}))
    time_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'time__from'}))
    time_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'time__to'}))
    name = forms.CharField(max_length=255, label='Name')