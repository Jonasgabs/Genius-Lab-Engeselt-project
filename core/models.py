from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractUser serve para os campos básicos de autenticação (nome de usuário, senha, etc.)

#instacia dos usuários
class Usuario(AbstractUser):
    is_admin = models.BooleanField(default=False) # pra saber se é admin ou nao 

    
#instancia para os livros
class Livro(models.Model):
    titulo = models.CharField(max_length=200) # campos de texto (CharField)
    autor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)  # saber se ta disponível 


#instancia para os empréstimos 
class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #chave de usuário estrangeira para o bd
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE) #chave de livro estrangeira para o bd
    data_emprestimo = models.DateField(auto_now_add=True) # add automaticamente (auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True) # opcional


# usar o django para mandar pro bd
#comandos pra não esquecer 
"""
criar -

python manage.py makemigrations

aplicar - 

python manage.py migrate


"""

