from django.urls import path
from . import views

#definindo as rotas para pag de login e lista de livros

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('login/', views.login_view, name='login'),
    path('livros/', views.lista_livros, name='lista_livros'),
]
