# livros/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def cadastrar_livro(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('leitor_dashboard')

    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.quantidade_disponivel = livro.quantidade_total
            livro.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = LivroForm()
    return render(request, 'livros/cadastrar_livro.html', {'form': form})

@login_required
def listar_livros_disponiveis(request):
    livros = Livro.objects.filter(quantidade_disponivel__gt=0)
    return render(request, 'livros/listar_livros_disponiveis.html', {'livros': livros})

@login_required
def inativar_livro(request, livro_id):
    if request.user.tipo_usuario != 'admin':
        return redirect('leitor_dashboard')

    livro = get_object_or_404(Livro, id=livro_id)
    livro.quantidade_disponivel = 0
    livro.save()
    messages.success(request, 'Livro inativado com sucesso!')
    return redirect('admin_dashboard')
