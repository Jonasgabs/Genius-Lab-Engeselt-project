# emprestimos/forms.py

from django import forms
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import Usuario

class RegistrarEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_devolucao_prevista']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar apenas livros disponíveis
        self.fields['livro'].queryset = Livro.objects.filter(quantidade_disponivel__gt=0)
        self.fields['usuario'].queryset = Usuario.objects.filter(tipo_usuario='leitor')

class DevolverEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['data_devolucao', 'observacoes']

class SolicitarEmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'data_devolucao_prevista']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar apenas livros disponíveis
        self.fields['livro'].queryset = Livro.objects.filter(quantidade_disponivel__gt=0)
