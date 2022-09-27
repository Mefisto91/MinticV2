
from dataclasses import fields
from appHospital.models.persona import tbl_persona
from rest_framework import serializers

class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_persona
        fields = ['id', 'usuario', 'contraseña', 'nombre', 'apellido', 'edad', 'id_rol']





