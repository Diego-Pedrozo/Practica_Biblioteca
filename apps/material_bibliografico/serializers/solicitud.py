from rest_framework import serializers
from apps.material_bibliografico.models.solicitud import SolicitudModel

class SolicitudSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitudModel
        fields = '__all__'

class SolicitudStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitudModel
        fields = ['estado']