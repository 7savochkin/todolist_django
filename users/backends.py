from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


UserModel = get_user_model()


class EmailModelBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(email=email)  # noqa
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(
                    user):
                return user


class PhoneModelBackend(ModelBackend):

    def authenticate(self, request, phone=None, password=None, **kwargs):
        if phone is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(phone=phone)  # noqa
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(
                    user):
                return user

    def user_can_authenticate(self, user):
        can_auth = super().user_can_authenticate(user)
        return can_auth and user.is_valid_phone
