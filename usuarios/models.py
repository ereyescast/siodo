from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User)

    direccion = models.TextField(
        blank=True,
        null=True
    )

    documento_identidad = models.CharField(
        max_length=10,
        blank=True,
        null=True)

    telefono = models.CharField(
        max_length=9,
        blank=True,
        null=True
    )

    fecha_nac = models.DateField(
        blank = True,
        null = True

    )
    avatar = models.ImageField(
        upload_to='avatar',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.usuario.username





class Estado(models.Model):
    idestado = models.CharField(
        primary_key=True,
        max_length=20
    )

    tipo_estado = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )



class Servicio(models.Model):
    idservicio = models.CharField(
        primary_key=True,
        max_length=20
    )
    nombre_servicio = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    tipservicio = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )
    duracion = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )



class Cita(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=20
    )

    num_historia = models.CharField(
        max_length=20
        , blank=True
        , null=True
    )

    hora_inicio = models.CharField(
        max_length=10
        , blank=True
        , null=True
    )

    hora_fin = models.CharField(
        max_length=10
        , blank=True
        , null=True
    )

    fecha = models.CharField(
        max_length=10
        , blank=True
        , null=True
    )
    idestado = models.ForeignKey(
        Estado
    , blank = True
    , null = True

    )

    turno = models.CharField(
        max_length=5
        , blank=True
        , null=True
    )
    idservicio = models.ForeignKey(Servicio
                                   , blank=True
                                   , null=True
                                   )

    def __str__(self):
        return self.idestado.idestado, self.idservicio.idservicio