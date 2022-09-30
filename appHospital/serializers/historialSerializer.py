
from dataclasses import fields

from rest_framework import serializers
from appHospital.models.historial import historialModel

class historialSerializer(serializers.ModelSerializer):

    class Meta: 
        model = historialModel
        fields = ['id', 'sugerencia', 'fecha', 'id_paciente']

  





