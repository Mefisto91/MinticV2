

from enum import unique
from sqlite3 import Timestamp
from django.db import models

from appHospital.models.persona import personaModel 
from appHospital.models.paciente import pacienteModel

class historialModel(models.Model):
    id = models.AutoField(primary_key = True);
    id_paciente = models.ForeignKey(pacienteModel, on_delete=models.RESTRICT);
    sugerencia = models.CharField(max_length = 50);
    fecha = models.DateField();



