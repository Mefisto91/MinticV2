
from django.db import models
from .paciente import tbl_paciente

class tbl_signovital(models.Model):
    id = models.SmallIntegerField(primary_key=True);
    id_paciente = models.ForeignKey(tbl_paciente, on_delete=models.RESTRICT)
    oximetria = models.SmallIntegerField();
    frec_respiratoria = models.SmallIntegerField();
    frec_cardiaca = models.SmallIntegerField();
    temperatura = models.SmallIntegerField();
    presion_arterial = models.SmallIntegerField();
    glicemias = models.SmallIntegerField();
    fecha = models.DateField();



