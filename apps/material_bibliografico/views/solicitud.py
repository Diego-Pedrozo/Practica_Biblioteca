from rest_framework.viewsets import ModelViewSet
from apps.material_bibliografico.models.solicitud import SolicitudModel
from apps.material_bibliografico.serializers.solicitud import SolicitudSerializer, SolicitudStatusUpdateSerializer

from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.response import Response
# from datetime import date, datetime
# from django.db.models import Q


class SolicitudPublicViewSet(ModelViewSet):
    model = SolicitudModel
    serializer_class = SolicitudSerializer
    queryset = SolicitudModel.objects.all()    
    http_method_names = ['get', 'post']

    
    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            data_solicitud = request.data
            serializer_solicitud = SolicitudSerializer(data=data_solicitud)

            if serializer_solicitud.is_valid():
                solicitud = serializer_solicitud.save()
                return Response({'mensaje': 'Solicitud creada'}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'mensaje': 'Error de solicitud', 'info': serializer_solicitud.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'mensaje': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)

class SolicitudViewSet(ModelViewSet):
    model = SolicitudModel
    serializer_class = SolicitudSerializer
    queryset = SolicitudModel.objects.all()    
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch', 'delete']
    
    def partial_update(self, request, *args, **kwargs):
        print(self.action)
        try:
            instance = self.get_object()
            user = self.request.user
            user_information = UserInformationModel.objects.get(user=user)
            data_estado = request.data
            serializer_solicitud = SolicitudStatusUpdateSerializer(data=data_estado)

            if user_information.user_type not in ['5']:
                return Response({'mensaje': 'No tiene permisos para cambiar el estado de la solicitud'}, status=status.HTTP_403_FORBIDDEN)
            
            else:
                if serializer_solicitud.is_valid():
                    instance.estado = data_estado.get('estado')
                    instance.save()
                    return Response({'mensaje': 'Estado actualizado'}, status=status.HTTP_200_OK)
                else:
                    return Response({'mensaje': 'Estado no valido'}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'mensaje': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        
        id_solicitud = instance.id
        SolicitudModel.objects.filter(id=id_solicitud).delete()

        return Response({'mensaje': 'Solicitud eliminada'}, status=status.HTTP_200_OK)

