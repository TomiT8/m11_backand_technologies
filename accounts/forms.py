from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Užívatelské jméno',
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'email': 'Email',
            'password1': 'Heslo',
            'password2': 'Heslo znovu'
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Heslo'}),
        label="Heslo"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Heslo znovu'}),
        label="Heslo znovu"
    )
