from rest_framework import serializers
from apps.material_bibliografico.models.propuestas_excel import PropuestasExcelModel

class PropuestasExcelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropuestasExcelModel
        fields = '__all__'