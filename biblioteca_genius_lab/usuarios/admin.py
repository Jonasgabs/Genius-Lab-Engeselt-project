from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'tipo_usuario', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo_usuario', 'endereco', 'telefone')}),
    )

admin.site.register(Usuario, UsuarioAdmin)