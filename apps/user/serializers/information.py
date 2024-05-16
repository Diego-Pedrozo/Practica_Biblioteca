from apps.user.models.information import UserInformationModel
from rest_framework import serializers

#More information for user model
class InformationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['identification', 'user_type', 'user_facultad', 'user_programa']

class InformationUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['identification', 'user_type', 'user', 'user_facultad', 'user_programa']

class InformationUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformationModel
        fields = ['user_type']
