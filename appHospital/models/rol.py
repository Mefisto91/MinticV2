
from django.db import models

class rolModel(models.Model):
    id = models.AutoField(primary_key=True);
    rol = models.CharField(max_length=15);