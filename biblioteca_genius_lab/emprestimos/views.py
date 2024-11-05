from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroEmprestimoForm, DevolucaoEmprestimoForm
from .models import Emprestimo
from livros.models import Livro
from django.utils import timezone
from django.contrib import messages

def is_admin(user):
    return user.tipo_usuario == 'admin'

@login_required
@user_passes_test(is_admin)
def registro_emprestimo(request):
    if request.method == 'POST':
        form = RegistroEmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            livro = emprestimo.livro
            if livro.quantidade_disponivel > 0:
                livro.quantidade_disponivel -= 1
                livro.save()
                emprestimo.save()
                messages.success(request, "Empréstimo registrado com sucesso!")
                return redirect('index')
            else:
                form.add_error('livro', 'Este livro não está disponível para empréstimo.')
    else:
        form = RegistroEmprestimoForm()
    return render(request, 'emprestimos/registro_emprestimo.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def devolucao_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id, status='aberto')
    if request.method == 'POST':
        form = DevolucaoEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.status = 'concluido'
            emprestimo.save()
            livro = emprestimo.livro
            livro.quantidade_disponivel += 1
            livro.save()
            messages.success(request, "Devolução registrada com sucesso!")
            return redirect('index')
    else:
        form = DevolucaoEmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimos/devolucao_emprestimo.html', {'form': form, 'emprestimo': emprestimo})

@login_required
@user_passes_test(is_admin)
def relatorio_emprestimos(request):
    emprestimos = None
    if request.method == 'POST':
        data_inicio = request.POST.get('data_inicio')
        data_fim = request.POST.get('data_fim')
        emprestimos = Emprestimo.objects.filter(
            data_emprestimo__range=[data_inicio, data_fim]
        )
    return render(request, 'emprestimos/relatorio.html', {'emprestimos': emprestimos})