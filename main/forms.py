from django import forms
from main import views


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your firstname'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your lastname'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your email address'}))
    subject = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your subject of this message'}))
    message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={
        'cols': '30', 'class': 'form-control', 'placeholder': 'Say something about us'}))

