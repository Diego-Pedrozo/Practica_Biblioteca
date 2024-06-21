from django.db import models
from django.utils.translation import gettext as _

class PropuestasExcelModel(models.Model):
    titulo = models.TextField(verbose_name=_('Título'), help_text=_(''), null=False, unique=False, default='')
    url = models.TextField(max_length=500, verbose_name=_('Url'), help_text=_(''), null=False, unique=False, blank= False, default='')
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.file}, {self.uploaded_at}'
    
    class Meta:
        verbose_name = _('Propuesta excel')
        verbose_name_plural= _('Propuestas excel')