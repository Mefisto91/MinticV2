

from appHospital.models.familiar import tbl_familiar
from rest_framework import serializers

class familiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_familiar
        fields = ['id', 'email']







