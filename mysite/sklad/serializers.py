from calendar import month

from rest_framework import serializers
from .models import *


class ExelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exel
        fields = '__all__'

