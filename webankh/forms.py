from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        print(">> confirm_login_allowed ejecutado para:", user)
        if not user.is_active:
            raise forms.ValidationError(
                "Tu cuenta está pendiente de aprobación.",
                code='inactive',
            )

    def get_invalid_login_error(self):
        return forms.ValidationError(
            "Usuario o contraseña incorrectos.",
            code="invalid_login",
        )