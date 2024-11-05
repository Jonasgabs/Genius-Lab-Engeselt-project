from django import forms
from .models import Emprestimo
from livros.models import Livro
from usuarios.models import Usuario
from django.utils import timezone

class RegistroEmprestimoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(tipo_usuario='leitor'),
        label="Usuário"
    )
    livro = forms.ModelChoiceField(
        queryset=Livro.objects.filter(quantidade_disponivel__gt=0),
        label="Livro"
    )
    data_devolucao_prevista = forms.DateField(
        widget=forms.SelectDateWidget,
        label="Data de Devolução Prevista"
    )
    status = forms.ChoiceField(
        choices=Emprestimo.STATUS_CHOICES,
        initial='aberto',
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_devolucao_prevista', 'status']

    def clean_data_devolucao_prevista(self):
        data_prevista = self.cleaned_data.get('data_devolucao_prevista')
        if data_prevista < timezone.now().date():
            raise forms.ValidationError("A data de devolução prevista não pode ser no passado.")
        return data_prevista

class DevolucaoEmprestimoForm(forms.ModelForm):
    data_devolucao_real = forms.DateField(
        widget=forms.SelectDateWidget,
        label="Data de Devolução Real"
    )
    observacoes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        label="Observações"
    )

    class Meta:
        model = Emprestimo
        fields = ['data_devolucao_real', 'observacoes']

    def clean_data_devolucao_real(self):
        data_real = self.cleaned_data.get('data_devolucao_real')
        if data_real < self.instance.data_emprestimo:
            raise forms.ValidationError("A data de devolução real não pode ser anterior à data de empréstimo.")
        return data_real