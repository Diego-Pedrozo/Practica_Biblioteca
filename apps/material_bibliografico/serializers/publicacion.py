from rest_framework import serializers
from apps.material_bibliografico.models.publicacion import PublicacionModel

class PublicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicacionModel
        fields = '__all__'
