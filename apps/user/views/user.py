from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from apps.user.serializers.user import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from apps.user.models.information import UserInformationModel
from apps.user.serializers.information import InformationUserSerializer

# Usuarios CRUD
class UserViewSet(ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ IsAuthenticated ]
    
    def get_queryset(self):
        queryset = User.objects
        user_id = self.request.user.id
        queryset = queryset.filter(id=user_id)
        
        return queryset
    
    def partial_update(self, request, *args, **kwargs):
        print('Actualizar datos')
        instance = self.get_object()
        information_data = request.data.pop('information', None)

        instance.first_name = request.data.get('first_name', instance.first_name)
        instance.last_name = request.data.get('last_name', instance.last_name)
        
        password = request.data.get('password', None)
        if password:
            instance.set_password(password)

        if information_data:
            identification = information_data.get('identification')
            if UserInformationModel.objects.filter(identification=identification).exclude(user=instance).exists():
                return Response({"mensaje": "El documento ingresado ya esta en uso"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                information_serializer = InformationUserSerializer(instance.information, data=information_data, partial=True)
                if information_serializer.is_valid():
                    information_serializer.save()
                instance.save()
                return Response({"mensaje": "Datos actualizados"}, status=status.HTTP_200_OK)