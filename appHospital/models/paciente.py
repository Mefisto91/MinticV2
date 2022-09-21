
from django.db import models
from .persona import tbl_persona
from .familiar import tbl_familiar

class tbl_paciente(models.Model):
    id = models.ForeignKey(tbl_persona, primary_key=True, on_delete=models.RESTRICT);
    direccion = models.CharField(max_length=30);
    id_familiar = models.ForeignKey(tbl_familiar, on_delete=models.RESTRICT);
    id_medico = models.SmallIntegerField();

