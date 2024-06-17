from rest_framework.viewsets import ModelViewSet
from apps.material_bibliografico.models.notificacion import NotificacionModel
from apps.material_bibliografico.serializers.notificacion import NotificacionSerializer, NotificacionCreateSerializer
from apps.material_bibliografico.models.solicitud import SolicitudModel

from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.response import Response
import json
from ..paginators import CustomPaginator
# from datetime import date, datetime
# from django.db.models import Q


class NotificacionViewSet(ModelViewSet):
    model = NotificacionModel
    serializer_class = NotificacionSerializer
    queryset = NotificacionModel.objects.all()    
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def list(self, request, *args, **kwargs):
        paginator = CustomPaginator()
        user = self.request.user
        user_information = UserInformationModel.objects.get(user=user)

        if user_information.user_type in ['4']:
            qs = self.get_queryset().filter(destinario='Decano', facultad=user_information.user_facultad).order_by('-id')  
        if user_information.user_type in ['5']:
            qs = self.get_queryset().filter(destinario='Biblioteca', facultad=user_information.user_facultad).order_by('-id')  

        # qs = self.get_queryset().order_by('id')  
        result_page = paginator.paginate_queryset(qs, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data) 

        # user = self.request.user
        # user_information = UserInformationModel.objects.get(user=user)
        # queryset = NotificacionModel.objects.filter(destinario=user)
        # serializer = self.get_serializer(queryset, many=True)
        #return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            data_notificacion = request.data.copy()
            #user_biblioteca = UserInformationModel.objects.filter(user_type='5').first()
            # if not user_biblioteca:
            #     return Response({'mensaje': 'No se encontró un usuario con el rol 5 (Biblioteca)'}, status=status.HTTP_404_NOT_FOUND)
            
            data_notificacion['destinario'] = 'Biblioteca'

            ids_solicitudes = json.loads(data_notificacion.get('ids_solicitudes', '[]'))
            serializer_notificacion = NotificacionCreateSerializer(data=data_notificacion)

            if not ids_solicitudes:
                return Response({'mensaje': 'Se requiere al menos un ID de solicitud'}, status=status.HTTP_400_BAD_REQUEST)
            
            #user = data_notificacion.get('destinario')
            # user_information = UserInformationModel.objects.get(user=user)

            # if user_information.user_type not in ['4', '5']:
            #     return Response({'mensaje': 'El destinatario debe tener uno de los siguientes roles: 4.Decano, 5.Biblioteca'}, status=status.HTTP_403_FORBIDDEN)

            if serializer_notificacion.is_valid():
                notificacion = serializer_notificacion.save()

                user = self.request.user
                user_information = UserInformationModel.objects.get(user=user)
                
                if user_information.user_type in ['6']:
                    solicitudes_a_actualizar = SolicitudModel.objects.filter(id__in=ids_solicitudes, nivel_revision='4').values_list('id', flat=True)
                    nuevo_nivel_revision = '5'
                                        
                    if solicitudes_a_actualizar:
                        solicitudes_a_actualizar = SolicitudModel.objects.filter(id__in=solicitudes_a_actualizar)
                        solicitudes_a_actualizar.update(nivel_revision=nuevo_nivel_revision)
                    else: 
                        notificacion.delete()
                        return Response({'mensaje': 'Se requieren solicitudes validas para actualizar'}, status=status.HTTP_400_BAD_REQUEST)


                return Response({'mensaje': 'Notificación creada'}, status=status.HTTP_201_CREATED)
            
            else:
                notificacion.delete()
                return Response({'mensaje': 'Error de notificación', 'info': serializer_notificacion.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            notificacion.delete()
            return Response({'mensaje': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)
    
        
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        instance.delete()

        return Response({'mensaje': 'Notificación eliminada'}, status=status.HTTP_200_OK)

