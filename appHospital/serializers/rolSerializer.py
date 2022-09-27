
from dataclasses import fields
from appHospital.models.rol import tbl_rol
from rest_framework import serializers

class rolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = tbl_rol
        fields = ['id', 'rol']


