from rest_framework import serializers
from apps.material_bibliografico.models.solicitud import SolicitudModel, LibroModel

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibroModel
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    libro = LibroSerializer(many=False, read_only=True)

    class Meta:
        model = SolicitudModel
        fields = '__all__'

class SolicitudCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitudModel
        fields = '__all__'

class SolicitudStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitudModel
        fields = ['estado']

class SolicitudLevelUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SolicitudModel
        fields = ['nivel']