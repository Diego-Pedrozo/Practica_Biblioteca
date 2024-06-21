from django.db import models
from django.utils.translation import gettext as _

class UserRanges(models.TextChoices):
    ADMIN = 1, _('Administrador')
    DIRECTOR_ESTUDIOS = 2, _('Director plan de estudios')
    DIRECTOR_DEPARTAMENTO = 3, _('Director de departamento')
    DECANO = 4, _('Decano')
    BIBLIOTECA = 5, _('Biblioteca')
    #VICERRECTOR = 6, _('Vicerrector')

    @classmethod
    def get_name(cls, value):
        for choice in cls.choices:
            if choice[0] == value:
                return choice[1]
        return None

class UserFacultad(models.TextChoices):
    CIENCIAS_AGRARIAS_AMBIENTE = 1, _('Ciencias Agrarias y del Ambiente') # Ingeniería Agroindustrial, Ingeniería Agronómica, Ingeniería Ambiental, Ingeniería Biotecnológica, Zootecnia 
    CIENCIAS_BASICAS = 2, _('Ciencias Básicas') #Química Industrial
    CIENCIAS_EMPRESARIALES = 3, _('Ciencias Empresariales') #Administración de Empresas, Contaduría Pública, Comercio Internacional
    CIENCIAS_DE_SALUD = 4, _('Ciencias de salud') #Enfermería, Seguridad y Salud en el Trabajo 
    EDUCACION_ARTES_HUMANIDADES = 5, _('Educación, Artes y Humanidades') #Comunicación Social, Trabajo Social, Derecho, Arquitectura
    INGENIERIA = 6, _('Ingeniería') #Ingeniería Civil, Ingeniería de Sistemas, Ingeniería Electrónica, Ingeniería Electromecánica, Ingeniería Industrial, Ingeniería de Minas, Ingeniería Mecánica

    @classmethod
    def get_name(cls, value):
        for choice in cls.choices:
            if choice[0] == value:
                return choice[1]
        return None

class UserPrograma(models.TextChoices):
    ING_AGROINDUSTRIAL = 1, _('Ingeniería Agroindustrial')
    ING_AGRONOMICA = 2, _('Ingeniería Agronómica')
    ING_AMBIENTAL = 3, _('Ingeniería Ambiental')
    ING_BIOTECNOLOGICA = 4, _('Ingeniería Biotecnológica')
    ZOOTECNIA = 5, _('Zootecnia')#
    QUIMICA_INDUSTRIAL = 6, _('Química Industrial')#
    ADMINISTRACION_EMPRESAS = 7, _('Administración de Empresas')
    CONTADURIA_PUBLICA = 8, _('Contaduría Pública')
    COMERCIO_INTERNACIONAL = 9, _('Comercio Internacional')#
    ENFERMERIA = 10, _('Enfermería')
    SEGURIDAD_SALUD_TRABAJO = 11, _('Seguridad y Salud en el Trabajo')#
    COMUNICACION_SOCIAL = 12, _('Comunicación Social')
    TRABAJO_SOCIAL = 13, _('Trabajo Social')
    DERECHO = 14, _('Derecho')
    ARQUITECTURA = 15, _('Arquitectura')#
    ING_CIVIL = 16, _('Ingeniería Civil')
    ING_SISTEMAS = 17, _('Ingeniería de Sistemas')
    ING_ELECTRONICA = 18, _('Ingeniería Electrónica')
    ING_ELECTROMECANICA = 19, _('Ingeniería Electromecánica')
    ING_INDUSTRIAL = 20, _('Ingeniería Industrial')
    ING_MINAS = 21, _('Ingeniería de Minas')
    ING_MECANICA = 22, _('Ingeniería Mecánica')#

    @classmethod
    def get_name(cls, value):
        for choice in cls.choices:
            if choice[0] == value:
                return choice[1]
        return None
    
class NivelRevision(models.TextChoices):
        CREADA = 1, _('Creada y enviada')  #solicitud creada y enviada a directores de departamento y plan de estudios
        ENVIADA_DECANO = 2, _('Solicitud enviada a decano') #solicitud enviada a decano
        ENVIADA_BIBLIOTECA = 3, _('Solicitud enviada a biblioteca') #solicitud enviada a biblioteca
        ENVIADA_VICERRECTOR = 4, _('Solicitud enviada a vicerrector') #solicitud enviada a vicerrector
        APROBADA = 5, _('Aprobada') #solicitudes aprobadas por vicerrector y enviadas a biblioteca para que actualicen el estado
        RECHAZADA = 6, _('Rechazada') #solicitudes rechazadas por vicerrector y enviadas a biblioteca para que actualicen el estado