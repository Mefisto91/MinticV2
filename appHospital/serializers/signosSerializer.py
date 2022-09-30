
from rest_framework import serializers
from appHospital.models.signos import signosModel

class signosSerializer(serializers.ModelSerializer):

    class Meta: 
        model = signosModel
        fields = '__all__'

  





