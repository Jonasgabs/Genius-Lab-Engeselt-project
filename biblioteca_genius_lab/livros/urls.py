# livros/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('listar/', views.listar_livros_disponiveis, name='listar_livros_disponiveis'),
    path('inativar/<int:livro_id>/', views.inativar_livro, name='inativar_livro'),
]
