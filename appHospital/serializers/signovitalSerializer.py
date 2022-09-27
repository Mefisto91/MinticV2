
from dataclasses import fields
from appHospital.models.signovital import tbl_signovital
from rest_framework import serializers

class signovitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_signovital
        fields = ['id_paciente', 'oximetria', 'frec_respiratoria']

