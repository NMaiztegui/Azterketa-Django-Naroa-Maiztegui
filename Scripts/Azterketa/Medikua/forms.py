from django import forms
from .models import Pazientea,Medikua,Zitak

class MedikuaForm(forms.ModelForm):
    class Meta:
        models=Medikua
        fields=['izena','abizena']

class PazienteaForms(forms.ModelForm):
    class Meta:
        models=Pazientea
        fields=['izena','abizena','dni']

