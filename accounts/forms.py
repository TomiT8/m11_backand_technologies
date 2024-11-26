from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import DateField, NumberInput, CharField, PasswordInput, Textarea

from accounts.models import Profile


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

    password1 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo'}),
        label="Heslo"
    )
    password2 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo znovu'}),
        label="Heslo znovu"
    )

    date_of_birth = DateField(
        widget=NumberInput(attrs={'type': 'date'}),
        label='Datum narození',
        required=False
    )

    biography = CharField(
        widget=Textarea,
        label='Biografie',
        required=False
    )
    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)

        date_of_birth = self.cleaned_data['date_of_birth']
        biography = self.cleaned_data['biography']
        profile = Profile(user=user,
                          date_of_birth=date_of_birth,
                          biography=biography)

        if commit:
            profile.save()
        return user
