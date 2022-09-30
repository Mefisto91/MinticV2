
from pyexpat import model
from django.db import models

from appHospital.models.persona import personaModel

class familiarModel(models.Model):
    id = models.ForeignKey(personaModel, on_delete=models.RESTRICT, primary_key = True);
    email = models.CharField(max_length = 30);

