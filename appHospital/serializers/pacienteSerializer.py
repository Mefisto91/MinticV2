
from dataclasses import fields
from appHospital.models.paciente import tbl_paciente
from rest_framework import serializers

class pacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_paciente
        fields = ['id', 'direccion', 'id_familiar', 'id_medico']




