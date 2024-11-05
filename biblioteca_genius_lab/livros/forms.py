from django import forms
from .models import Livro

class CadastroLivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'editora', 'ano_publicacao', 'genero', 'quantidade_total', 'descricao']

    def clean_quantidade_total(self):
        quantidade_total = self.cleaned_data.get('quantidade_total')
        if quantidade_total < 0:
            raise forms.ValidationError('A quantidade total não pode ser negativa.')
        return quantidade_total

    def save(self, commit=True):
        livro = super().save(commit=False)
        livro.quantidade_disponivel = livro.quantidade_total
        if commit:
            livro.save()
        return livro