from rest_framework import serializers
from apps.material_bibliografico.models.fechas_limite import FechasLimiteModel

class FechasLimiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = FechasLimiteModel
        fields = '__all__'