
from dataclasses import fields
from appHospital.models.rol import rolModel
from rest_framework import serializers

class rolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = rolModel
        fields = '__all__'

    def create(self, validated_data):
        rol = rolModel.objects.create(**validated_data)
        rolModel.objects.create(rol=rol)
        return rol

    def to_representation(self, obj):
        rol = rolModel.objects.get()
        return{
            'rol': rol.id
        }