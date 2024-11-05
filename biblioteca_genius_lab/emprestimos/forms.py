from django import forms
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import Usuario

class RegistroEmprestimoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.filter(tipo_usuario='leitor'))
    livro = forms.ModelChoiceField(queryset=Livro.objects.filter(quantidade_disponivel__gt=0))
    data_emprestimo = forms.DateField(widget=forms.SelectDateWidget)
    data_devolucao_prevista = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_emprestimo', 'data_devolucao_prevista', 'status']

class DevolucaoEmprestimoForm(forms.ModelForm):
    data_devolucao_real = forms.DateField(widget=forms.SelectDateWidget)
    observacoes = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Emprestimo
        fields = ['data_devolucao_real', 'observacoes']