from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class StylesCustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "new_password1",
                "id": "new_password1",
                "placeholder": _("New password"),
            }
        ),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "new_password2",
                "id": "new_password2",
                "placeholder": _("Confirm your new password"),
            }
        ),
    )


class StylesCustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "email",
                "id": "email",
                "placeholder": _("Email"),
            }
        ),
    )


class StylesCustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        max_length=128, min_length=8, required=True,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "autofocus": True,
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "old_password",
                "id": "old_password",
                "placeholder": _("Your old password"),
            }
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        max_length=128, min_length=8, required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "new_password1",
                "id": "new_password1",
                "placeholder": _("New password"),
            }
        ),
    )

    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        max_length=128, min_length=8, required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "new_password2",
                "id": "new_password2",
                "placeholder": _("Confirm your new password"),
            }
        ),
    )

    class Meta:
        model = User
        fields = "__all__"


class StylesCustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=150, required=True, label=_("First Name"), widget=forms.TextInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "first_name",
                "id": "first_name",
                "placeholder": _("First Name"),
            }
        )
    )
    last_name = forms.CharField(
        max_length=150, required=True, label=_("Last Name"), widget=forms.TextInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "last_name",
                "id": "last_name",
                "placeholder": "Last Name",
            }
        )
    )

    email = forms.EmailField(
        disabled=True, required=True, label=_("Email"), widget=forms.EmailInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "email",
                "id": "email",
                "placeholder": _("Email"),
            }
        )
    )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class StylesCustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150, required=True, label=_("First Name"), widget=forms.TextInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "first_name",
                "id": "first_name",
                "placeholder": _("First Name"),
            }
        )
    )
    last_name = forms.CharField(
        max_length=150, required=True, label=_("Last Name"), widget=forms.TextInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "last_name",
                "id": "last_name",
                "placeholder": _("Last Name"),
            }
        )
    )

    email = forms.EmailField(
        required=True, label=_("Email"), widget=forms.EmailInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "email",
                "id": "email",
                "placeholder": _("Email"),
            }
        )
    )

    username = forms.CharField(
        max_length=150, label=_("Username"), required=True, widget=forms.TextInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "username",
                "id": "username",
                "placeholder": _("Username"),
            }
        )
    )
    password1 = forms.CharField(
        max_length=128, min_length=8, label=_("Password"), required=True, widget=forms.PasswordInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "password1",
                "id": "password1",
                "placeholder": "********",
            }
        )
    )
    password2 = forms.CharField(
        max_length=128, min_length=8, label=_("Confirm Password"), required=True, widget=forms.PasswordInput(
            attrs={
                "class": "form-control border-always outline-0 shadow-0 lh-lg",
                "name": "password2",
                "id": "password2",
                "placeholder": "********",
            }
        )
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2", ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = "__all__"
