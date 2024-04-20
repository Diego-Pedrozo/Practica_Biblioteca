from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class SolicitudModel(models.Model):
    #info libro
    titulo = models.CharField(max_length=50, verbose_name=_('Título'), help_text=_(''), null=False, unique=False)
    autor = models.CharField(max_length=50, verbose_name=_('Autor/es'), help_text=_(''), null=False, unique=False)
    editorial = models.CharField(max_length=50, verbose_name=_('Editorial'), help_text=_(''), null=False, unique=False)
    edicion = models.CharField(max_length=50, verbose_name=_('Edición'), help_text=_(''), null=False, unique=False)
    ejemplares = models.IntegerField(verbose_name=_('Ejemplares'), help_text=_(''), null=False, unique=False)
    fecha_publicacion = models.DateField(max_length=50, verbose_name=_('Fecha de publicación'), help_text=_(''), null=False, unique=False)
    IDIOMA_CHOICES = [
        ('Español', 'Español'),
        ('Ingles', 'Ingles'),
    ] 
    idioma = models.CharField(max_length=50, verbose_name=_('Idioma'), help_text=_(''), choices=IDIOMA_CHOICES, default='', null=False, unique=False)

    #info extra
    facultad = models.CharField(max_length=50, verbose_name=_('Facultad'), help_text=_(''), null=False, unique=False)
    programa_academico = models.CharField(max_length=50, verbose_name=_('Programa académico'), help_text=_(''), null=False, unique=False)
    anotacion = models.CharField(max_length=300, verbose_name=_('Anotación'), help_text=_(''), null=False, default='No aplica', unique=False, blank= True)
    SOLICITANTE_CHOICES = [
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
    ] 
    solicitante = models.CharField(max_length=50, verbose_name=_('Solicitante'), help_text=_(''), choices=SOLICITANTE_CHOICES, default='', null=False, unique=False)

    #info verificacion
    ESTADO_CHOICES = [
        ('Existente', 'Existente'),
        ('En tramite', 'En trámite'),
        ('Inexistente', 'Inexistente'),
        ('Sin revisar', 'Sin revisar')
    ]
    estado = models.CharField(max_length=50, verbose_name=_('Estado'), help_text=_(''), choices=ESTADO_CHOICES, default='Sin revisar', null=False, unique=False)

    def __str__(self) -> str:
        return f'{self.id}, {self.titulo}, {self.estado}'
    
    class Meta:
        verbose_name = _('Solicitud')
        verbose_name_plural= _('Solicitudes')
