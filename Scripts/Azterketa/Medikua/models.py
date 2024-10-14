from django.db import models
from django.utils import timezone
# Create your models here.

class Medikua(models.Model):
    id=models.AutoField(primary_key=True)
    izena=models.CharField(max_length=100)
    abizena=models.CharField(max_length=100)
    

    def __str__(self):
        return f'{self.izena}-{self.abizena}'

class Pazientea(models.Model):
    id=models.AutoField(primary_key=True)
    izena=models.CharField(max_length=100)
    abizena=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.izena}-{self.abizena}-{self.dni}'

class Zitak(models.Model):
    
    mediku=models.ForeignKey(Medikua,on_delete=models.CASCADE)
    pazientea=models.ForeignKey(Pazientea, on_delete=models.CASCADE)
    ordua=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.mediku}-{self.pazientea}-{self.ordua}'
