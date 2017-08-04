from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    usuario = models.OneToOneField(User)

    direccion = models.TextField(
        blank=False,
        null=False
    )

    documento_identidad = models.CharField(
        max_length=10,
        blank=False,
        null=False)

    telefono = models.CharField(
        max_length=9,
        blank=False,
        null=False
    )

    fecha_nac = models.DateField()

    avatar = models.ImageField(
        upload_to='avatar',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.usuario.username

class Cita(models.Model):
    num_historia = models.ForeignKey(User)

    def __str__(self):
        return self.num_historia.id