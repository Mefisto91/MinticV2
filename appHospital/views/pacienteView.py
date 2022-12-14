

from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.pacienteSerializer import pacienteSerializer

class pacienteView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = pacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)



