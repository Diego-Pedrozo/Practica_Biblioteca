from django.db import models
from django.utils.translation import gettext as _

class PublicacionModel(models.Model):
    #info publicacion
    imagen = models.ImageField(verbose_name=('Imagen'),upload_to='publicaciones/',  max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=50, verbose_name=_('Título'), help_text=_(''), null=False, unique=False)
    descripcion = models.CharField(max_length=50, verbose_name=_('Descripción'), help_text=_(''), null=False, unique=False)

    def __str__(self) -> str:
        return f'{self.id}, {self.titulo}, {self.descripcion}'
    
    class Meta:
        verbose_name = _('Publicación')
        verbose_name_plural= _('Publicaciones')

