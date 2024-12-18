import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea, ModelForm, NumberInput

from viewer.models import Country, Creator, Movie

"""
class CreatorForm(Form):
    first_name = CharField(max_length=32, required=False)
    last_name = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    nationality = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)
"""


class CreatorForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        #fields = ['biography', 'first_name', 'last_name']
        #exclude = ['nationality']
        labels = {
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'nationality': 'Národnost',
            'biography': "Biografie"
        }
        help_texts = {
            'biography': "Zde zadejte biografii tvůrce."
        }
        error_messages = {
            # TO DO
        }

    #first_name = CharField(max_length=32, required=False, label='Jméno')
    #last_name = CharField(max_length=32, required=False, label='Příjmení')
    date_of_birth = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}), label='Datum narození')
    date_of_death = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}), label='Datum úmrtí')
    #nationality = ModelChoiceField(queryset=Country.objects, required=False, label='Národnost')
    #biography = CharField(widget=Textarea, required=False, label="Biografie")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_first_name(self):
        """ Upraví zadané jméno tak, aby začínalo velkým písmenem. """
        initial = self.cleaned_data['first_name']
        print(f"Initial = '{initial}'")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result  = '{result}'")
        return result

    def clean_last_name(self):
        """ Upraví zadané příjmení tak, aby začínalo velkým písmenem. """
        initial = self.cleaned_data['last_name']
        print(f"Initial = '{initial}'")
        result = initial
        if initial:
            result = initial.capitalize()
            print(f"result  = '{result}'")
        return result

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        print(f"Initial = '{initial}'")
        if initial and initial > date.today():
            raise ValidationError("Lze zadávat datum narození pouze v minulosti.")
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        print(f"Initial = '{initial}'")
        if initial and initial > date.today():
            raise ValidationError("Lze zadávat datum úmrtí pouze v minulosti.")
        return initial

    def clean_biography(self):
        # Force each sentence of the biography to be capitalized.
        initial = self.cleaned_data['biography']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        initial_first_name = cleaned_data['first_name']
        initial_last_name = cleaned_data['last_name']
        print(f"initial_first_name = '{initial_first_name}', initial_last_name = '{initial_last_name}'")
        if not initial_first_name and not initial_last_name:
            raise ValidationError("Je potřeba zadat jméno nebo příjmení (nebo oboje).")

        initial_date_of_birth = cleaned_data['date_of_birth']
        initial_date_of_death = cleaned_data['date_of_death']
        if initial_date_of_birth and initial_date_of_death and initial_date_of_death <= initial_date_of_birth:
            raise ValidationError("Datum úmrtí nemůže být dřív, než datum narození.")

        return cleaned_data


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title_orig', 'title_cz', 'year', 'length', 'directors', 'actors', 'countries', 'genres', 'description']
        labels = {
            'title_orig': 'Originálny názov',
            'title_cz': 'Český názov',
            'year': 'Rok',
            'length': 'Dĺžka (min)',
            'directors': 'Réžie',
            'actors': 'Herecké obsadenie',
            'countries': 'Krajiny',
            'genres': 'Žánre',
            'description': 'Popis',
        }
        help_texts = {
            'title_orig': 'Zadajte originálny názov filmu.',
            'title_cz': 'Zadajte český názov filmu (ak existuje).',
            'year': 'Zadajte rok vydania filmu.',
            'length': 'Dĺžka filmu v minútach.',
            'description': 'Popis filmu, stručný obsah alebo iné detaily.',
        }
        error_messages = {
            'title_orig': {
                'required': 'Tento údaj je povinný.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_year(self):
        year = self.cleaned_data['year']
        if year and year > date.today().year:
            raise ValidationError("Rok filmu nemôže byť v budúcnosti.")
        return year

    def clean_length(self):
        length = self.cleaned_data['length']
        if length and length <= 0:
            raise ValidationError("Dĺžka filmu musí byť väčšia než 0.")
        return length

    def clean(self):
        cleaned_data = super().clean()

        title_orig = cleaned_data.get('title_orig')
        if not title_orig:
            raise ValidationError("Originálny názov je povinný.")

        return cleaned_data
