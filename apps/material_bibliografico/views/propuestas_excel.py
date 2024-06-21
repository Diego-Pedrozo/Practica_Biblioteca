from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.material_bibliografico.models.propuestas_excel import PropuestasExcelModel
from apps.material_bibliografico.serializers.propuestas_excel import PropuestasExcelSerializer
from rest_framework.permissions import IsAuthenticated
from ..paginators import CustomPaginator

class PropuestasExcelViewSet(viewsets.ModelViewSet):
    model = PropuestasExcelModel
    serializer_class = PropuestasExcelSerializer
    queryset = PropuestasExcelModel.objects.all()    
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']

    def list(self, request, *args, **kwargs):
        paginator = CustomPaginator()
        qs = self.get_queryset().order_by('-id')
        result_page = paginator.paginate_queryset(qs, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data) 
    
    def create(self, request, *args, **kwargs):
        print(self.action)
        try:
            data_propuesta = request.data
            serializer_propuesta = PropuestasExcelSerializer(data=data_propuesta)

            if serializer_propuesta.is_valid():
                propuesta = serializer_propuesta.save()
                return Response({'mensaje': 'Propuesta creada'}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'mensaje': 'Error de creación', 'info': serializer_propuesta.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'mensaje': 'Error de creación', 'info': {str(e)}}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        print(self.action)
        instance = self.get_object()
        instance.delete()

        return Response({'mensaje': 'Propuesta eliminada'}, status=status.HTTP_200_OK)


