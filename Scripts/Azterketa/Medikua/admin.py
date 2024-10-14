from django.contrib import admin
from .models import Pazientea, Medikua, Zitak
# Register your models here.
admin.site.register([Pazientea,Medikua,Zitak])