# livros/admin.py

from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'quantidade_total', 'quantidade_disponivel')
    search_fields = ('titulo', 'autor', 'isbn')

admin.site.register(Livro, LivroAdmin)
