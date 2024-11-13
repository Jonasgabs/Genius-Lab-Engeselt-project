# emprestimos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('devolver/', views.devolver_emprestimo, name='devolver_emprestimo'),
    path('pendentes/', views.listar_emprestimos_pendentes, name='listar_emprestimos_pendentes'),
    path('aprovar/<int:emprestimo_id>/', views.aprovar_emprestimo, name='aprovar_emprestimo'),
    path('relatorio/', views.relatorio_emprestimos, name='relatorio_emprestimos'),
    path('solicitar/', views.solicitar_emprestimo, name='solicitar_emprestimo'),
    path('historico/', views.historico_emprestimos, name='historico_emprestimos'),
]
