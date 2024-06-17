from rest_framework import serializers
from apps.material_bibliografico.models.notificacion import NotificacionModel
from apps.user.serializers.user import UserSerializer


class NotificacionSerializer(serializers.ModelSerializer):
    #destinario = UserSerializer(many=False, read_only=True)

    class Meta:
        model = NotificacionModel
        fields = ['id', 'fecha_notificacion', 'descripcion', 'archivo', 'destinario', 'facultad']

class NotificacionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificacionModel
        fields = '__all__'
