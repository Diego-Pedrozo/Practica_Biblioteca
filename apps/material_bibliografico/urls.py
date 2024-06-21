from django.urls import path, include
from rest_framework import routers
from apps.material_bibliografico.views.solicitud import SolicitudViewSet, SolicitudPublicViewSet
from apps.material_bibliografico.views.publicacion import PublicacionPublicViewSet, PublicacionViewSet
from apps.material_bibliografico.views.notificacion import NotificacionViewSet
from apps.material_bibliografico.views.fechas_limite import FechasLimiteViewSet

app_name = 'material_bibliografico'
router = routers.DefaultRouter()
#Configurar rutas 
router.register(viewset=SolicitudViewSet, prefix='solicitud', basename='solicitud')
router.register(viewset=SolicitudPublicViewSet, prefix='solicitud_public', basename='solicitud_public')
router.register(viewset=PublicacionViewSet, prefix='publicacion', basename='publicacion')
router.register(viewset=PublicacionPublicViewSet, prefix='publicacion_public', basename='publicacion_public')
router.register(viewset=NotificacionViewSet, prefix='notificacion', basename='notificacion')
router.register(viewset=FechasLimiteViewSet, prefix='fechas_limite', basename='fechas_limite')


urlpatterns = [
    path('', include(router.urls))   
]