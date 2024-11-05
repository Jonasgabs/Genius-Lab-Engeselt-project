from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_emprestimo, name='registro_emprestimo'),
    path('devolucao/<int:emprestimo_id>/', views.devolucao_emprestimo, name='devolucao_emprestimo'),
    path('relatorio/', views.relatorio_emprestimos, name='relatorio_emprestimos'),
]