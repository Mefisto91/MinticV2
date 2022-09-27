
from appHospital.models.historia import tbl_historia
from rest_framework import serializers

class historiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_historia
        fields = ['id', 'id_paciente', 'sugerencia', 'fecha']



