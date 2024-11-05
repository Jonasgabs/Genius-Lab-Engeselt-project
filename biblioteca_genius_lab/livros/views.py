from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CadastroLivroForm
from .models import Livro

def is_admin(user):
    return user.tipo_usuario == 'admin'

@login_required
@user_passes_test(is_admin)
def cadastro_livro(request):
    if request.method == 'POST':
        form = CadastroLivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CadastroLivroForm()
    return render(request, 'livros/cadastro_livro.html', {'form': form})