from django import forms
from django.forms import ModelForm
from .models import pulistan


class pu(forms.Form):

    val = (
        ('Ja', 'Ja'),
        ('Nej', 'Nej'),
    )

    manader = (
        ('Januari', 'Januari'),
        ('Februari', 'Februari'),
        ('Mars', 'Mars'),
        ('April', 'April'),
        ('Maj', 'Maj'),
        ('Juni', 'Juni'),
        ('Juli', 'Juli'),
        ('Augusti', 'Augusti'),
        ('September', 'September'),
        ('Oktober', 'Oktober'),
        ('November', 'November'),
        ('December', 'December'),
    )
    avd = forms.CharField(
        max_length=100,
        label='Driftsektion',
    )

    beskrivning = forms.CharField(max_length=50, label='PU-namn:')
    artal = forms.CharField(max_length=20, label='Årtal')
    kostnad = forms.CharField(max_length=20, required=False, label='Anslagsbelopp:')
    projektnr = forms.CharField(max_length=20, required=False, label='Projektnr:')
    projektledare = forms.CharField(max_length=20, required=False, label='Projektledare:')
    projektansvarig = forms.CharField(max_length=20, required=False, label='Projektansvarig:')
    ansvar = forms.CharField(max_length=7, required=False, label='Ansvar:')
    motpart = forms.CharField(max_length=20, required=False, label='Motpart:')
    b_start = forms.CharField(max_length=20, required=False, label='Beräknad start:')
    b_klart = forms.CharField(max_length=20, required=False, label='Beräknad färdig:')
    objektid = forms.CharField(max_length=20, required=False, label='Objekt-ID:')
    arbetsorder = forms.CharField(max_length=20, required=False, label='AO-nr:')
    beviljan_m = forms.ChoiceField(choices=manader, required=False, label='Önskat beviljn mån:')
    rs = forms.ChoiceField(required=False,choices=val, label='Kräver revisionstopp?')
    motivering = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}),max_length=500)
    omfattning = forms.CharField(max_length=500, required=False)
    konsekvens = forms.CharField(widget=forms.Textarea(attrs={"rows" : 5, "cols" : 20}), max_length=500)

class RedigeraForm(forms.Form) :

    avd = forms.CharField(max_length=20, required=True, label="Avd:")
    beskrivning = forms.CharField(max_length=20, required=True, label="Beskrivning:")
    artal = forms.CharField(max_length=20, required=True, label="Årtal:")
    kostnad = forms.CharField(max_length=20, required=True, label="Kostnad:")
    projektnr = forms.CharField(max_length=20, required=True, label="Projektnr:")


class Update(ModelForm):
    class Meta:
        model = pulistan
        fields = ['avd', 'beskrivning', 'artal']