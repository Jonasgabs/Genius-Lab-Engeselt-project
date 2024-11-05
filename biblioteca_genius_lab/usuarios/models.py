from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = (
        ('admin', 'Administrador'),
        ('leitor', 'Leitor'),
    )
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username