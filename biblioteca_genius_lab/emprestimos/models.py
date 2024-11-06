# emprestimos/models.py

from django.db import models
from livros.models import Livro
from usuarios.models import Usuario

class Emprestimo(models.Model):
    STATUS_CHOICES = (
        ('aberto', 'Em Aberto'),
        ('concluido', 'Concluído'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField('Data do Empréstimo', auto_now_add=True)
    data_devolucao_prevista = models.DateField('Data de Devolução Prevista')
    data_devolucao = models.DateField('Data de Devolução', null=True, blank=True)
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='aberto')
    observacoes = models.TextField('Observações', blank=True, null=True)

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.usuario.nome_completo}"

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Novo empréstimo
            self.livro.quantidade_disponivel -= 1
            self.livro.save()
        super(Emprestimo, self).save(*args, **kwargs)
