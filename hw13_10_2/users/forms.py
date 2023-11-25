from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    # first_name = forms.CharField(
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Name"}
    #     ),
    # )

    # last_name = forms.CharField(
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "LastName"}
    #     ),
    # )

    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )

    password1 = forms.CharField(
        label="Password",
        max_length=20,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )

    password2 = forms.CharField(
        label="Password confirmation",
        max_length=20,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", 
                  "email", 
                #   "first_name", 
                #   "last_name", 
                  "password1", 
                  "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )

    password = forms.CharField(
        max_length=20,
        min_length=6,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class DeleteForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = [
            "username",
        ]

# class ProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.FileInput())

#     class Meta:
#         model = Profile
#         fields = ['avatar']        