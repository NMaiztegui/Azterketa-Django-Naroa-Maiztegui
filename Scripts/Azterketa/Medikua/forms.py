from django import forms
from .models import Pazientea,Medikua,Zitak

class MedikuaForm(forms.ModelForm):
    class Meta:
        model=Medikua
        fields=['izena','abizena']

class PazienteaForms(forms.ModelForm):
    class Meta:
        model=Pazientea
        fields=['izena','abizena','dni']

class ZitakForms(forms.ModelForm):
    class Meta:
        model=Zitak
        fields=['mediku','pazientea','ordua']

class MedikuaAldatuForm(forms.ModelForm):
    class Meta:
        model=Medikua
        fields=['izena','abizena']
    