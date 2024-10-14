from rest_framework import viewsets
from .serializers import *


class ExelViewSet(viewsets.ModelViewSet):
    queryset = Exel.objects.all()
    serializer_class = ExelSerializers

