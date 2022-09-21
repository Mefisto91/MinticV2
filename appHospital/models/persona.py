
from mailbox import NoSuchMailboxError
from django.db import models
from .rol import tbl_rol

class tbl_persona(models.Model):
    id = models.SmallIntegerField(primary_key=True);
    nombre = models.CharField(max_length=15);
    apellido = models.CharField(max_length=15);
    edad = models.SmallIntegerField();
    id_rol = models.ForeignKey(tbl_rol, on_delete=models.RESTRICT);


