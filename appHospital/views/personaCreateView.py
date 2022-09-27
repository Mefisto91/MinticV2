
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from appHospital.serializers.personaSerializer import personaSerializer

class personaCreateView(views.APIView):
   
    def post(self, request, *args, **kwargs):
        serializer = personaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"usuario":request.data["usuario"],
                    "contraseña":request.data["contraseña"]}

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

