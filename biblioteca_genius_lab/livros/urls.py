from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_livro, name='cadastro_livro'),
]