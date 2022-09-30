
from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.familiarSerializer import familiarSerializer

class familiarView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = familiarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
