
from django.db import models
from .persona import tbl_persona

class tbl_familiar(models.Model):
    id = models.ForeignKey(tbl_persona, primary_key=True, on_delete=models.RESTRICT);
    email = models.CharField(max_length=50);

