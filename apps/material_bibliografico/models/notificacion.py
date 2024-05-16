from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from datetime import date
from apps.material_bibliografico.models.solicitud import SolicitudModel
   
class NotificacionModel(models.Model):
    fecha_notificacion= models.DateField(verbose_name=_('Fecha de notificación'), help_text=_(''), null=False, unique=False, default=date.today)
    descripcion = models.CharField(max_length=300, verbose_name=_('Anotación'), help_text=_(''), null=False, unique=False, blank= False)
    archivo = models.FileField(verbose_name=_('Archivo'), help_text=_(''), null=True, unique=False, blank= True)
    destinario = models.ForeignKey(User, verbose_name=_('Destinatario'), help_text=_(''), null=False, unique=False, on_delete=models.CASCADE, related_name='destinario')


    def __str__(self) -> str:
        return f'{self.id}, {self.fecha_notificacion}, {self.descripcion}, {self.archivo}'
    
    class Meta:
        verbose_name = _('Notificación')
        verbose_name_plural= _('Notificaciones')

