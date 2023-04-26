import re

from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.core.exceptions import ValidationError

User = get_user_model()


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': ' '}),
            'phone': forms.TextInput(attrs={'placeholder': ' '}),
            'password': forms.PasswordInput(attrs={'placeholder': ' '})
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['email'].required = False
        # self.fields['phone'].required = False

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        phone = self.cleaned_data.get('phone')

        if not email and not phone:
            self.errors.update({
                'ValidationError': 'Email or phone number label is required'
            })
            raise ValidationError('Email or phone number are required')
        if password:
            kwargs = {'password': password, 'email': email}
            if not email:
                kwargs.pop('email')
                kwargs['phone'] = phone
            user = authenticate(**kwargs)
            if user is None:
                self.errors.update({
                    'AuthenticationError': 'User is not found'
                })
                raise ValidationError('User is not signed up')
            else:
                login(self.request, user)
        return self.cleaned_data


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': ' '}))
    phone = forms.CharField(label='Phone Number', max_length=17,
                            widget=forms.TextInput(
                                attrs={'placeholder': ' '}))
    first_password = forms.CharField(label='Password',
                                     widget=forms.PasswordInput(
                                         attrs={'placeholder': ' '}))
    second_password = forms.CharField(label='Confirm Password',
                                      widget=forms.PasswordInput(
                                          attrs={'placeholder': ' '}))

    def clean(self):
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        first_password = self.cleaned_data['first_password']
        second_password = self.cleaned_data['second_password']

        try:
            is_existed = User.objects.get(email=email)
        except User.DoesNotExist:
            is_existed = False

        if not email or not phone:
            self.errors.update({
                'ValidationError': 'Email and phone number label is required'
            })
            raise ValidationError('Email or phone number are required')
        elif not re.fullmatch(r'^\+?1?\d{9,15}$', phone):
            self.errors.update({
                'ValidationError': 'Phone should be +11111111'
            })
            raise ValidationError('Phone should be +11111111')
        elif is_existed:
            self.errors.update({
                'ValidationError': 'This user is already exists'
            })
            raise ValidationError('This user is already exists')
        elif not first_password or not second_password:
            self.errors.update({
                'ValidationError': 'Password label is required'
            })
            raise ValidationError('Email or phone number are required')
        elif first_password != second_password:
            self.errors.update({
                'ValidationError': 'Password must be matched'
            })
            raise ValidationError('Password must be matched')
        elif not re.fullmatch(
                r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",
                first_password):  # noqa
            self.errors.update({
                'ValidationError': 'Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:' # noqa
            })
            raise ValidationError(
                'Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:')  # noqa
        return super().clean()

    def save(self):
        new_user = User.objects.create(
            email=self.cleaned_data['email'], phone=self.cleaned_data['phone'])
        new_user.is_valid_phone = True
        new_user.set_password(self.cleaned_data['first_password'])
        new_user.save()
        return new_user
