
from dataclasses import fields

from rest_framework import serializers
from appHospital.models.familiar import familiarModel

from appHospital.models.persona import personaModel

class familiarSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 30)

    class Meta: 
        model = personaModel
        fields = ['id', 'username', 'password', 'nombre', 'apellido', 'edad', 'id_rol', 'email']

    def create(self, validated_data):
        emailSave = validated_data.pop('email')
        
        personaInstance = personaModel.objects.create(**validated_data)
        familiarModel.objects.create(id=personaInstance, email=emailSave)
        return personaInstance





