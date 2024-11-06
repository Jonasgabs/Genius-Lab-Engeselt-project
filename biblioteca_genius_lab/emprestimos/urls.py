# emprestimos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('devolver/', views.devolver_emprestimo, name='devolver_emprestimo'),
    path('relatorio/', views.relatorio_emprestimos, name='relatorio_emprestimos'),
    path('solicitar/', views.solicitar_emprestimo, name='solicitar_emprestimo'),
    path('historico/', views.historico_emprestimos, name='historico_emprestimos'),
]
