from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from UUID_gen_app.models import Data
from UUID_gen_app.serializer import DataSerializer


class DataAPIView(APIView):
    serializers_class = DataSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = dict()
        Data.objects.create()
        queryset = Data.objects.all()
        serializer = self.serializers_class(queryset, many=True)

        for instance in serializer.data:
            data[instance['created_at']] = instance['id']

        return Response(data, status=status.HTTP_200_OK)
