
from django.db import models

class tbl_rol(models.Model):
    id = models.SmallIntegerField(primary_key=True);
    rol = models.CharField(max_length=15);