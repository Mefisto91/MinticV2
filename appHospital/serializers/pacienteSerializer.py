

from dataclasses import fields

from rest_framework import serializers
from appHospital.models.paciente import pacienteModel

from appHospital.models.persona import personaModel
from appHospital.models.familiar import familiarModel
from appHospital.serializers.familiarSerializer import familiarSerializer

class pacienteSerializer(serializers.ModelSerializer):
    direccion = serializers.CharField(max_length = 50)
    id_familiar = serializers.IntegerField()

    class Meta: 
        model = personaModel
        fields = ['id', 'username', 'password', 'nombre', 'apellido', 'edad', 'id_rol', 
                'direccion', 'id_familiar']

    def create(self, validated_data):
        direccionSave = validated_data.pop('direccion')
        idFamilarSave = validated_data.pop('id_familiar')

        personaInstance = personaModel.objects.create(**validated_data)
        pacienteModel.objects.create(id=personaInstance, direccion=direccionSave, id_familiar_id=idFamilarSave)
        return personaInstance







