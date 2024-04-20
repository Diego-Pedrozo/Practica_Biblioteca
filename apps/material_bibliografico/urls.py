from django.urls import path, include
from rest_framework import routers
from apps.material_bibliografico.views.solicitud import SolicitudViewSet, SolicitudPublicViewSet

app_name = 'material_bibliografico'
router = routers.DefaultRouter()
#Configurar rutas 
router.register(viewset=SolicitudViewSet, prefix='solicitud', basename='solicitud')
router.register(viewset=SolicitudPublicViewSet, prefix='solicitud_public', basename='solicitud_public')


urlpatterns = [
    path('', include(router.urls))   
]