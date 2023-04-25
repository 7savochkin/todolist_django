# from django.contrib.auth.views import LoginView
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ValidationError

from base.validators import PhoneValidator

User = get_user_model()


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'password')
        field_classes = {'email': UsernameField}

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        phone = self.cleaned_data.get('phone')

        if not email:
             raise ValidationError('Email or phone number is required')
        if password:
            kwargs = {'password': password, 'email': email}
            user = authenticate()
