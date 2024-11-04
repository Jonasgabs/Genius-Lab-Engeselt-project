from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Livro 
from .forms import LoginForm

# render e redirect pra exibir páginas HTML ou redirecionar o usuário para outra página.

# login_required pra visualização só se tiver logado

# so vai mostrar a lista se tiver logado fi
@login_required
def lista_livros(request):
    livros = Livro.objects.all()#pega todos os livros que tem no bd
    return render(request, 'lista_livros.html', {'livros': livros}) #renderizar a pág com os livros 


def login_view(request):
    if request.method == 'POST': # para autenticar os dados de login que são pegados são form
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) #autenticando
            if user is not None: # se conseguir logar vai para a pagina com a lista de livros
                login(request, user)
                return redirect('lista_livros')
    else: #se for get vai mostrar o formulario para login vazio
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request): #pagina inicial
    return render(request, 'home.html')

