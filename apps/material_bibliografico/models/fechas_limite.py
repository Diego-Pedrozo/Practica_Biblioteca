from django.db import models
from django.utils.translation import gettext as _

class FechasLimiteModel(models.Model):
    fecha_inicio = models.DateField(verbose_name=_('Fecha inicio de solicitudes'), help_text=_(''), null=False, unique=False)
    fecha_fin = models.DateField(verbose_name=_('Fecha fin de solicitudes'), help_text=_(''), null=False, unique=False)

    def __str__(self) -> str:
        return f'{self.id}, {self.fecha_inicio}, {self.fecha_fin}'
    
    class Meta:
        verbose_name = _('Fecha limite')
        verbose_name_plural= _('Fechas limmite')
    

