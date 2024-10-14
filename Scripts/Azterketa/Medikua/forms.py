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

class PazienteaEditatu(forms.ModelForm):
    class Meta:
        model=Pazientea
        fields=['izena','abizena','dni']
    
    def __init__(self, *args, **kwargs):
        super(PazienteaEditatu,self).__init__(*args, **kwargs)
        if self.instance:
         
          self.fields['dni'].disabled = True 
class ZitaEditatuForm(forms.ModelForm):
    class Meta:
        model=Zitak
        fields=['mediku','pazientea','ordua']
    
    def __init__(self, *args, **kwargs):
        super(ZitaEditatuForm,self).__init__(*args, **kwargs)
        if self.instance:
         
          self.fields['pazientea'].disabled = True 
