# livros/models.py

from django.db import models

class Livro(models.Model):
    GENEROS_CHOICES = (
        ('ficcao', 'Ficção'),
        ('nao-ficcao', 'Não-Ficção'),
        ('romance', 'Romance'),
        ('ciencia', 'Ciência'),
        
    )

    titulo = models.CharField('Título', max_length=200)
    autor = models.CharField('Autor', max_length=200)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    editora = models.CharField('Editora', max_length=200)
    ano_publicacao = models.PositiveIntegerField('Ano de Publicação')
    genero = models.CharField('Gênero', max_length=50, choices=GENEROS_CHOICES)
    quantidade_total = models.PositiveIntegerField('Quantidade Total')
    quantidade_disponivel = models.PositiveIntegerField('Quantidade Disponível', default=0)
    descricao = models.TextField('Descrição', blank=True, null=True)

    def __str__(self):
        return self.titulo
