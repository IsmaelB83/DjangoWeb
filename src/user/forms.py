# Python imports
# Django imports
from django import forms
# Third party app imports
# Local app imports
from .models import Author


class LoginForm(forms.ModelForm):
    user = forms.CharField(label='Username', required=True, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'username', 'autocomplete': 'off'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'off'}))


class SocialForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('location', 'description', 'birth_date', 'image')
