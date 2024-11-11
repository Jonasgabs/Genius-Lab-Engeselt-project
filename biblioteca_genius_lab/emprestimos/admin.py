# emprestimos/admin.py

from django.contrib import admin
from .models import Emprestimo

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_emprestimo', 'data_devolucao_prevista', 'status')
    search_fields = ('livro__titulo', 'usuario__nome_completo')
    list_filter = ('status',)

admin.site.register(Emprestimo, EmprestimoAdmin)
