from django import forms
from django.forms import ModelForm, widgets
from .models import Namnlista


class NameForm(forms.Form):
    avd_val = (
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('18', '18'),
    )
    las_lista_val = (
        ('Svart', 'Svart'),
        ('Vit', 'Vit'),
        ('Blå', 'Blå'),
        ('Gul', 'Gul'),
        ('Röd', 'Röd'),
    )
    ao= forms.CharField(label='AO-nr:',required=False,
        widget=forms.TextInput(attrs={'readonly' : 'readonly'})
    )
    direktiv = forms.CharField(max_length=100)
    objektid = forms.CharField(max_length=20)
    avd = forms.ChoiceField(choices=avd_val)
    las_lista = forms.ChoiceField(choices=las_lista_val)


class UpdateForm(forms.Form) :
    las_lista_val = (
        ('Svart', 'Svart'),
        ('Vit', 'Vit'),
        ('Blå', 'Blå'),
        ('Gul', 'Gul'),
        ('Röd', 'Röd'),
    )

    operator = forms.CharField(max_length=20, required=True, label="Operatör:")
    las_lista = forms.ChoiceField(choices=las_lista_val, label="Låslista:")
    avstallt = forms.BooleanField(required=False, label="Avställning / Bryt & lås utfört")


class SigneraForm(forms.Form) :

    utforare = forms.CharField(max_length=12, label='ANST-nr / SSG-nr:')
    status = forms.HiddenInput


class Update(ModelForm):
    class Meta:
        model = Namnlista
        fields = ['avstallt', 'operator', 'las_lista']

class Signera(ModelForm):
    class Meta:
        model = Namnlista
        fields = ['utforare', 'status']
