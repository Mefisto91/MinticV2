
from django.db import models

from appHospital.models.paciente import pacienteModel

class signosModel(models.Model):
    id = models.AutoField(primary_key = True);
    id_paciente = models.ForeignKey(pacienteModel, on_delete=models.RESTRICT);
    oximetria = models.IntegerField();
    f_respiratoria = models.IntegerField();
    f_cardiaca = models.IntegerField();
    temperatura = models.IntegerField();
    presion_arterial = models.IntegerField();
    glicemias = models.IntegerField();
    fecha = models.DateField();