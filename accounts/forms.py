from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

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
        widgets = {
            'password1': PasswordInput(attrs={'placeholder': 'Heslo'}),
            'password2': PasswordInput(attrs={'placeholder': 'Heslo znovu'}),
        }
