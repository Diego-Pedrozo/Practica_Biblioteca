from django.db import models
from django.utils.translation import gettext as _

class UserRanges(models.TextChoices):
    ADMIN = 1, _('Administrador')
    DIRECTOR_ESTUDIOS = 2, _('Director plan de estudios')
    DIRECTOR_DEPARTAMENTO = 3, _('Director de departamento')
    DECANO = 4, _('Decano')
    BIBLIOTECA = 5, _('Biblioteca')
    VICERRECTOR = 6, _('Vicerrector')