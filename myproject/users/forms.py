from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Додаємо класи до полів
        self.fields['username'].widget.attrs.update({
            'class': 'input_login_form',
            'placeholder': 'Введіть ваш логін',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'input_login_form',
            'placeholder': 'Пароль',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input_login_form',
            'placeholder': 'Підтвердження пароля',
        })


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Додаємо класи до полів
        self.fields['username'].widget.attrs.update({
            'class': 'input_login_form',
            'placeholder': 'Логін',
        })
        self.fields['username'].label = "Логін"
        self.fields['password'].widget.attrs.update({
            'class': 'input_login_form',
            'placeholder': 'Пароль',
        })
        self.fields['password'].label = 'Пароль'

