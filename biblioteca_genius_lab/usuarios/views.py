# usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UsuarioCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('login')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.tipo_usuario == 'admin':
            return reverse_lazy('admin_dashboard')
        else:
            return reverse_lazy('leitor_dashboard')

@login_required
def admin_dashboard(request):
    if request.user.tipo_usuario != 'admin':
        return redirect('leitor_dashboard')
    return render(request, 'usuarios/admin_dashboard.html')

@login_required
def leitor_dashboard(request):
    if request.user.tipo_usuario != 'leitor':
        return redirect('admin_dashboard')
    return render(request, 'usuarios/leitor_dashboard.html')
