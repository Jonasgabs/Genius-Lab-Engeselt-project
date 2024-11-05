from django.db import models

class Livro(models.Model):
    GENERO_CHOICES = (
        ('ficcao', 'Ficção'),
        ('nao_ficcao', 'Não-Ficção'),
        ('romance', 'Romance'),
        ('ciencia', 'Ciência'),
        # Adicione mais gêneros conforme necessário
    )

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    editora = models.CharField(max_length=255)
    ano_publicacao = models.PositiveIntegerField()
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    quantidade_total = models.PositiveIntegerField()
    quantidade_disponivel = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo