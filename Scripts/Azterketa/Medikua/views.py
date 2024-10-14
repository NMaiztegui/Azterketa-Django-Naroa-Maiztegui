from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q 
from django.contrib import messages
from .models import Medikua, Pazientea, Zitak
from .forms import MedikuaForm, PazienteaForms,MedikuaAldatuForm,ZitakForms,PazienteaEditatu,ZitaEditatuForm

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
     medikua=Medikua.objects.get(id=kod_medikua)
     if request.method=='POST':
         medikua.delete()
         messages.success(request,'Medikua ezabatua')
         return redirect('medikuak_zerrenda')

def zita_new(request):
    if request.method=='POST':
        form=ZitakForms(request.POST)
        if form.is_valid():
            paziente=form.cleaned_data.get('pazientea')
            medikua=form.cleaned_data.get('mediku')
            ordu=form.cleaned_data.get('ordua')

            #comprobar si existe una cita igual para el paciente

            cita_exits=Zitak.objects.filter(
                    Q(pazientea=paziente) & Q(mediku=medikua) &  Q(ordua=ordu)
            ).exists()

            if cita_exits:
                form.add_error('ordua', 'Pazienteak ba du cita bat mediku honekin ordu berdinean, ordua edo medikua aldatu.')
            else:
                form.save()
                return redirect('zitak-zerrenda')
        return render(request, 'formularioak/zitak_new.html',{'form':form})
        
    else:
        form=ZitakForms()
        return render(request, 'formularioak/zitak_new.html',{'form':form})
def zitak_list (request):
    zitak=Zitak.objects.all()
    return render(request, 'zerrenda/zitak_list.html', {'zitak':zitak})

def pazientea_editatu(request,kod_pazientea):
    pazientea=Pazientea.objects.get(id=kod_pazientea)
    if request.method == 'POST':
        form=PazienteaEditatu(request.POST, instance=pazientea)
        if form.is_valid():
             form.save()
        return redirect('pazienteak-zerrenda')
    else:
        form=PazienteaEditatu( instance=pazientea)
        return render(request, 'formularioak/pazientea_editatu.html', {'form':form})

def pazientea_ezabatu(request,kod_pazientea):
    pazientea=Pazientea.objects.get(id=kod_pazientea)
    if request.method=='POST':
         pazientea.delete()
         messages.success(request,'Pazientea ezabatua')
         return redirect('pazienteak-zerrenda')

def zita_editatu(request,kod_pazientea, kod_mediku):
    zita=Zitak.objects.get(pazientea_id=kod_pazientea, mediku_id=kod_mediku)
    if request.method == 'POST':
        form=ZitaEditatuForm(request.POST, instance=zita)
        if form.is_valid():
             form.save()
        return redirect('zitak-zerrenda')
    else:
        form=ZitaEditatuForm( instance=zita)
        return render(request, 'formularioak/zita_editatu.html', {'form':form})


def zita_ezabatu(request,kod_pazientea, kod_mediku):
    zita=Zitak.objects.get(pazientea_id=kod_pazientea, mediku_id=kod_mediku)
    if request.method=='POST':
         zita.delete()
         messages.success(request,'Zita ezabatua')
         return redirect('zitak-zerrenda')

