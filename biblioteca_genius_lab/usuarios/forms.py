from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Informe um e-mail válido.')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'tipo_usuario', 'endereco', 'telefone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email