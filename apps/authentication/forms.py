# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))
    # is_superuser = forms.BooleanField(
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             "placeholder": "Superuser",
    #             "class": "form-check-input"
    #         }
    #     ))
    # is_staff = forms.BooleanField(
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             "placeholder": "Staff",
    #             "class": "form-check-input"
    #         }
    #     ))
    # is_active = forms.BooleanField(
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             "placeholder": "Active",
    #             "class": "form-check-input"
    #         }
    #     ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','is_superuser','is_staff','is_active','first_name','last_name')

