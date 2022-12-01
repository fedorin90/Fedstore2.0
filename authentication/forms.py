from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your login'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Your password'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Your password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Repeat your password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Your username'}),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Your email'}),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Your password'}),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Repeat your password'}),
        # }


class ResetUserForm(PasswordResetForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your email'}))

    class Meta:
        model = User







