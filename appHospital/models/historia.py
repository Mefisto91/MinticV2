
from unittest.util import _MAX_LENGTH
from django.db import models
from .paciente import tbl_paciente

class tbl_historia(models.Model):
    id = models.SmallIntegerField(primary_key=True);
    id_paciente = models.ForeignKey(tbl_paciente, on_delete=models.RESTRICT);
    sugerencia = models.CharField(max_length=200);
    fecha = models.DateField();





