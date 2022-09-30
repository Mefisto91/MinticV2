
from enum import unique
from django.db import models

from appHospital.models.persona import personaModel 
from appHospital.models.familiar import familiarModel

class pacienteModel(models.Model):
    id = models.ForeignKey(personaModel, on_delete=models.RESTRICT, primary_key = True);
    direccion = models.CharField(max_length = 50);
    id_familiar = models.ForeignKey(familiarModel, on_delete=models.RESTRICT);

