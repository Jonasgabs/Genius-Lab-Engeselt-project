from django.db import models
from django.conf import settings
from livros.models import Livro

class Emprestimo(models.Model):
    STATUS_CHOICES = (
        ('aberto', 'Em Aberto'),
        ('concluido', 'Concluído'),
    )

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_prevista = models.DateField()
    data_devolucao_real = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo}"