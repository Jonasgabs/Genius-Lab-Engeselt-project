# emprestimos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import RegistrarEmprestimoForm, DevolverEmprestimoForm, SolicitarEmprestimoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.utils import timezone

@login_required
def registrar_emprestimo(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('leitor_dashboard')

    if request.method == 'POST':
        form = RegistrarEmprestimoForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                emprestimo = form.save()
                messages.success(request, 'Empréstimo registrado com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = RegistrarEmprestimoForm()
    return render(request, 'emprestimos/registrar_emprestimo.html', {'form': form})

@login_required
def devolver_emprestimo(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('leitor_dashboard')

    emprestimos_abertos = Emprestimo.objects.filter(status='aberto')
    if request.method == 'POST':
        emprestimo_id = request.POST.get('emprestimo_id')
        emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
        form = DevolverEmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            with transaction.atomic():
                emprestimo = form.save(commit=False)
                emprestimo.status = 'concluido'
                emprestimo.save()
                # Atualizar quantidade disponível
                emprestimo.livro.quantidade_disponivel += 1
                emprestimo.livro.save()
                messages.success(request, 'Devolução registrada com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = DevolverEmprestimoForm()
    return render(request, 'emprestimos/devolver_emprestimo.html', {'emprestimos': emprestimos_abertos, 'form': form})

@login_required
def relatorio_emprestimos(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('leitor_dashboard')

    emprestimos = Emprestimo.objects.all().order_by('-data_emprestimo')
    return render(request, 'emprestimos/relatorio_emprestimos.html', {'emprestimos': emprestimos})


@login_required
def solicitar_emprestimo(request):
    if request.user.tipo_usuario != 'leitor':
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = SolicitarEmprestimoForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                emprestimo = form.save(commit=False)
                emprestimo.usuario = request.user
                emprestimo.status = 'aberto'
                emprestimo.save()
                messages.success(request, 'Empréstimo solicitado com sucesso!')
            return redirect('leitor_dashboard')
    else:
        form = SolicitarEmprestimoForm()
    return render(request, 'emprestimos/solicitar_emprestimo.html', {'form': form})

@login_required
def historico_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    return render(request, 'emprestimos/historico_emprestimos.html', {'emprestimos': emprestimos})

@login_required
def aprovar_emprestimo(request, emprestimo_id):
    if request.user.tipo_usuario != 'leitor':
        return redirect('admin_dashboard')
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    if request.method == 'POST':
        emprestimo.status = 'Aprovado'
        emprestimo.data_aprovacao = timezone.now()
        emprestimo.save()
        messages.success(request, 'Empréstimo aprovado com sucesso.')
        return redirect('listar_emprestimos_pendentes')
    return render(request, 'emprestimos/aprovar_emprestimo.html', {'emprestimo': emprestimo})

@login_required
def listar_emprestimos_pendentes(request):
    if request.user.tipo_usuario != 'leitor':
        return redirect('admin_dashboard')
    emprestimos_pendentes = Emprestimo.objects.filter(status='Pendente')
    return render(request, 'emprestimos/emprestimos_pendentes.html', {'emprestimos_pendentes': emprestimos_pendentes})
