from django.shortcuts import render,redirect
from django.db.models import Q 
from django.contrib import messages
from .models import Medikua, Pazientea, Zitak
from .forms import MedikuaForm, PazienteaForms,MedikuaAldatuForm

# Create your views here.
def main_page(request):
    return render(request,'main_page.html')

def medikuak_list(request):
    medikuak=Medikua.objects.all()
    return render(request, 'zerrenda/medikuak_list.html', {'medikuak':medikuak})

def medikua_new(request):
    if request.method == 'POST':
        form=MedikuaForm(request.POST)
        if form.is_valid:
            ikasle = form.save()
            ikasle.save()
        return redirect('medikuak_zerrenda') #cuandoi los datos se guardan y se meten al servidor, vulev a enviar al la vista inicila
    else:
        form=MedikuaForm()
        return render(request, 'formularioak/medikua_new.html', {'form':form})

def pazienteak_list(request):
    pazienteak=Pazientea.objects.all()
    return render(request, 'zerrenda/pazienteak_list.html', {'pazienteak':pazienteak})

def pazientea_new(request):
    if request.method == 'POST':
        form=PazienteaForms(request.POST)
        if form.is_valid:
            ikasle = form.save()
            ikasle.save()
        return redirect('pazienteak-zerrenda') #cuandoi los datos se guardan y se meten al servidor, vulev a enviar al la vista inicila
    else:
        form=PazienteaForms()
        return render(request, 'formularioak/pazientea_new.html', {'form':form})

def medikua_aldatu(request,kod_medikua):
    medikua=Medikua.objects.get(id=kod_medikua)
    if request.method == 'POST':
        form=MedikuaAldatuForm(request.POST, instance=medikua)
        if form.is_valid():
             form.save()
        return redirect('medikuak_zerrenda')
    else:
        form=MedikuaAldatuForm( instance=medikua)
        return render(request, 'formularioak/medikua_aldatu.html', {'form':form})

def medikua_ezabatu(request,kod_medikua) :
    

