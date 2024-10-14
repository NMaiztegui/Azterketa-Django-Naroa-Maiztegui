from django.urls import path
from . import views
urlpatterns = [
 path('main/', views.main_page, name='orri-nagursia'),
 path('medikua/list/', views.medikuak_list, name='medikuak_zerrenda'),
 path('medikua/new/', views.medikua_new, name='medikua-new'),
 path('pazientea/list/', views.pazienteak_list, name='pazienteak-zerrenda'),
 path('pazientea/new/' , views.pazientea_new, name='pazientea-new'),
 path('medikua/aldatu/<int:kod_medikua>/', views.medikua_aldatu, name='medikua-aldatu' ),
 path('medikua/list/<int:kod_medikua>/', views.medikua_ezabatu, name='medikua-ezabatu' ),
 
]
