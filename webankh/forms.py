from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        print("Se ejecuta confirm_login_allowed para:", user.username)
        if not user.is_active:
            raise forms.ValidationError(
                "Tu cuenta está pendiente de aprobación.",
                code='inactive',
            )