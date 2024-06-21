from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.material_bibliografico.models.fechas_limite import FechasLimiteModel
from apps.material_bibliografico.serializers.fechas_limite import FechasLimiteSerializer
from rest_framework.permissions import IsAuthenticated

class FechasLimiteViewSet(ModelViewSet):
    model = FechasLimiteModel
    queryset = FechasLimiteModel.objects.all()
    serializer_class = FechasLimiteSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            fecha_limite = FechasLimiteModel.objects.first()
            serializer = FechasLimiteSerializer(fecha_limite)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FechasLimiteModel.DoesNotExist:
            return Response({"error": "Fechas límite no encontradas"}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        instance = FechasLimiteModel.objects.first()
        if instance:
            serializer = FechasLimiteSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje": "Fechas límite actualizadas", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"mensaje": "Error al actualizar las fechas límite", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            serializer = FechasLimiteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje": "Fechas límite establecidas", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"mensaje": "Error al establecer las fechas límite", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
