
from dataclasses import fields
from appHospital.models.persona import personaModel
from rest_framework import serializers


class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = personaModel
        fields = '__all__'

