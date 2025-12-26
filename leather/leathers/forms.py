from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import *
from users.models import *


class PersonalAreaForm(UserChangeForm):
    birth = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%d.%m.%Y', attrs={'class':
        'single-input', 'placeholder': 'Дата рождения'}), localize=True)

    class Meta:
        model = User
        fields = ('image', 'username', 'email', 'last_name', 'first_name', 'patronymic', 'birth', 'address', 'phone_number', 'merit')
        widgets = {
            'image': forms.FileInput(attrs={'class': 'single-input', 'placeholder': 'фото'}),
            'username': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Логин'}),
            'email': forms.EmailInput(attrs={'class': 'single-input', 'placeholder': 'Адрес электронной почты'}),
            'last_name': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Имя'}),
            'patronymic': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Отчество'}),
            'address': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Адрес проживания'}),
            'phone_number': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Номер телефона'}),
            'merit': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'О себе'}),
        }