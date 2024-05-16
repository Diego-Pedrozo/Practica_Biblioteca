from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from apps.user.choices import UserRanges, UserFacultad, UserPrograma

class UserInformationModel(models.Model):
    user = models.OneToOneField(User, 
                                 on_delete=models.CASCADE, 
                                 verbose_name=_('Usuario'), 
                                 help_text=_('Seleccione Usuario'),
                                 related_name='information', 
                                 null=True)
     
    identification = models.CharField(max_length=30, 
                              verbose_name=_('Número de identificación'), 
                              help_text=_('Ingresa número de identificación'), 
                              null=False, 
                              unique=True)
    
    user_type = models.CharField(max_length= 255,
                                 choices=UserRanges.choices,
                                 verbose_name=_('Tipo de usuario'),
                                 help_text='Seleccione un tipo de usuario',
                                 blank=False,
                                 null=False)
    
    user_facultad = models.CharField(max_length= 255,
                                 choices=UserFacultad.choices,
                                 verbose_name=_('Facultad'),
                                 help_text='Seleccione una facultad',
                                 blank=True,
                                 null=True)
    
    user_programa = models.CharField(max_length= 255,
                                 choices=UserPrograma.choices,
                                 verbose_name=_('Programa academico'),
                                 help_text='Seleccione un programa academico',
                                 blank=True,
                                 null=True)

    def __str__(self) -> str:
        return str(self.user) 
        
    class Meta:
        verbose_name = _('Información adicional')
        verbose_name_plural = _('Informaciones adicionales')
