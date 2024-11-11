# usuarios/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome_completo, tipo_usuario='leitor', password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um endereço de email válido.')
        email = self.normalize_email(email)
        user = self.model(email=email, nome_completo=nome_completo, tipo_usuario=tipo_usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome_completo, password=None, **extra_fields):
        extra_fields.setdefault('tipo_usuario', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nome_completo, password=password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPO_USUARIO_CHOICES = (
        ('admin', 'Administrador'),
        ('leitor', 'Leitor'),
    )

    email = models.EmailField('Email', unique=True)
    nome_completo = models.CharField('Nome Completo', max_length=255)
    tipo_usuario = models.CharField('Tipo de Usuário', max_length=10, choices=TIPO_USUARIO_CHOICES)
    endereco = models.CharField('Endereço', max_length=255, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True, null=True)

    is_active = models.BooleanField('Ativo', default=True)
    is_staff = models.BooleanField('Equipe', default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo']

    def __str__(self):
        return self.email
