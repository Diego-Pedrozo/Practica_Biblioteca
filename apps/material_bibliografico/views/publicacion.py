from rest_framework.viewsets import ModelViewSet
from apps.material_bibliografico.models.publicacion import PublicacionModel
from apps.material_bibliografico.serializers.publicacion import PublicacionSerializer

from django.contrib.auth.models import User
from apps.user.models.information import UserInformationModel
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.response import Response
from ..paginators import CustomPaginator
# from datetime import date, datetime
# from django.db.models import Q


class PublicacionPublicViewSet(ModelViewSet):
    model = PublicacionModel
    serializer_class = PublicacionSerializer
    queryset = PublicacionModel.objects.all()    
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        paginator = CustomPaginator()
        qs = self.get_queryset().order_by('-id')
        result_page = paginator.paginate_queryset(qs, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data) 

class PublicacionViewSet(ModelViewSet):
    model = PublicacionModel
    serializer_class = PublicacionSerializer
    queryset = PublicacionModel.objects.all()    
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'delete']

    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            data_publicacion = request.data
            serializer_publicacion = PublicacionSerializer(data=data_publicacion)

            if serializer_publicacion.is_valid():
                publicacion = serializer_publicacion.save()
                return Response({'mensaje': 'Publicación creada'}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'mensaje': 'Error de publicación', 'info': serializer_publicacion.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'mensaje': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)
    
        
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        instance.delete()

        return Response({'mensaje': 'Publicación eliminada'}, status=status.HTTP_200_OK)

