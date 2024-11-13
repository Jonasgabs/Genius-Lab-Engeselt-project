# Documentação Detalhada do Sistema de Biblioteca - Genius Lab
## Índice
### Introdução
#### Estrutura do Projeto
##### 2.1. Diretório Raiz
##### 2.2. Aplicativos Django
*Configurações do Projeto (settings.py)*
##### 3.1. Configurações Básicas
##### 3.2. Configuração do Banco de Dados
##### 3.3. Aplicativos Instalados
##### 3.4. Middleware
##### 3.5. Templates
##### 3.6. Arquivos Estáticos
*URLs do Projeto (urls.py)*
*Aplicativo usuarios*
##### 5.1. Modelos (models.py)
##### 5.2. Formulários (forms.py)
##### 5.3. Views (views.py)
##### 5.4. URLs (urls.py)
*Aplicativo livros*
##### 6.1. Modelos (models.py)
##### 6.2. Formulários (forms.py)
##### 6.3. Views (views.py)
##### 6.4. URLs (urls.py)
*Aplicativo emprestimos*
##### 7.1. Modelos (models.py)
##### 7.2. Formulários (forms.py)
##### 7.3. Views (views.py)
##### 7.4. URLs (urls.py)
*Templates*
##### 8.1. Herança de Templates
##### 8.2. Templates Específicos
*Fluxo de Dados no Sistema*
##### 9.1. Autenticação e Autorização
##### 9.2. Gerenciamento de Livros
##### 9.3. Gerenciamento de Empréstimos


### 1. Introdução
*Este documento fornece uma visão detalhada do sistema de biblioteca desenvolvido durante o estágio na Genius Lab. O sistema permite o gerenciamento de usuários, livros e empréstimos, utilizando o framework Django e um banco de dados PostgreSQL. O objetivo desta documentação é explicar cada componente do sistema, como os arquivos estão organizados, como eles se comunicam e o papel de cada variável.*



### 2. Estrutura do Projeto
*O projeto segue a estrutura padrão de um projeto Django, com algumas customizações para atender às necessidades específicas do sistema.*



### 2.1. Diretório Raiz


    biblioteca_genius_lab/
    ├── biblioteca_genius_lab/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── usuarios/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── livros/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── emprestimos/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   └── (outros templates)
    ├── static/
    │   └── css/
    │       └── styles.css
    ├── manage.py
    └── venv/


### 2.2. Aplicativos Django
###### O projeto é composto por três aplicativos principais:

*usuarios: Gerencia os usuários do sistema, incluindo autenticação e registro.*
*livros: Gerencia o cadastro e manutenção dos livros disponíveis na biblioteca.*
*emprestimos: Gerencia os empréstimos de livros aos usuários.*


### 3. Configurações do Projeto (settings.py)
*O arquivo settings.py contém todas as configurações do projeto Django.*


### 3.1. Configurações Básicas
*SECRET_KEY: Chave secreta usada para criptografar dados. Importante manter em segredo.*
*DEBUG: Define se o modo de depuração está ativo. Em desenvolvimento, é True. Em produção, deve ser False.*
*ALLOWED_HOSTS: Lista de hosts/domínios que podem servir a aplicação.*


### 3.2. Configuração do Banco de Dados
##### Configurado para usar PostgreSQL:

<python>

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'Genius_Lab_lib',
            'USER': 'postgres',
            'PASSWORD': 'senha',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

<python>

    ENGINE: Especifica o backend do banco de dados.
    NAME: Nome do banco de dados.
    USER: Nome do usuário do banco de dados.
    PASSWORD: Senha do usuário.
    HOST: Endereço do servidor de banco de dados.
    PORT: Porta de conexão.


### 3.3. Aplicativos Instalados
<python>

    INSTALLED_APPS = [
        'usuarios',
        'livros',
        'emprestimos',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]   
<python>

*Ordem Importante: O aplicativo usuarios é listado antes de django.contrib.auth para que o Django reconheça o modelo de usuário customizado.*


### 3.4. Middleware
Middleware são camadas que processam requisições e respostas.


    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]


### 3.5. Templates
Configurações para renderização de templates.



    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],  # Diretório dos templates
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Processadores de contexto padrão
                ],
            },
        },
    ]
<a name="3.6"></a>

### 3.6. Arquivos Estáticos
Configurações para servir arquivos estáticos.


    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / 'static']


### 4. URLs do Projeto (urls.py)
O arquivo urls.py na pasta biblioteca_genius_lab é o ponto de entrada para as rotas da aplicação.


    from django.contrib import admin
    from django.urls import path, include
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')

    urlpatterns = [
        path('', index, name='index'),
        path('admin/', admin.site.urls),
        path('usuarios/', include('usuarios.urls')),
        path('livros/', include('livros.urls')),
        path('emprestimos/', include('emprestimos.urls')),
    ]

path('', index, name='index'): Rota para a página inicial.
include('app.urls'): Inclui as rotas definidas em cada aplicativo.


### 5. Aplicativo usuarios
O aplicativo usuarios gerencia os usuários do sistema.



### 5.1. Modelos (models.py)
Define o modelo de usuário customizado.


    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class Usuario(AbstractUser):
        TIPO_USUARIO_CHOICES = (
            ('admin', 'Administrador'),
            ('leitor', 'Leitor'),
        )
        tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
        endereco = models.CharField(max_length=255, blank=True, null=True)
        telefone = models.CharField(max_length=20, blank=True, null=True)

        def __str__(self):
            return self.username

Herança de AbstractUser: Permite customizar o modelo de usuário padrão do Django.
Campos Adicionais:
tipo_usuario: Indica o tipo de usuário (administrador ou leitor).
endereco e telefone: Informações de contato.


### 5.2. Formulários (forms.py)
Define formulários para criação e atualização de usuários.


    from django import forms
    from .models import Usuario

    class UsuarioForm(forms.ModelForm):
        class Meta:
            model = Usuario
            fields = ['username', 'password', 'tipo_usuario', 'endereco', 'telefone']
            widgets = {
                'password': forms.PasswordInput(),
            }
UsuarioForm: Formulário baseado em ModelForm para criar e editar usuários.
Widgets: Personaliza o campo password para ser um campo de senha.


### 5.3. Views (views.py)
Contém as funções de visualização (views) para gerenciar usuários.


    from django.shortcuts import render, redirect
    from .forms import UsuarioForm
    from .models import Usuario

    def cadastro_usuario(request):
        if request.method == 'POST':
            form = UsuarioForm(request.POST)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.set_password(form.cleaned_data['password'])
                usuario.save()
                return redirect('index')
        else:
            form = UsuarioForm()
        return render(request, 'cadastro_usuario.html', {'form': form})
cadastro_usuario:
GET: Exibe o formulário de cadastro.
POST: Processa o formulário e cria um novo usuário.
usuario.set_password(): Criptografa a senha.


### 5.4. URLs (urls.py)
Define as rotas para o aplicativo usuarios.


from django.urls import path
from . import views

    urlpatterns = [
        path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
        path('login/', views.login_usuario, name='login_usuario'),
        path('logout/', views.logout_usuario, name='logout_usuario'),
    ]
Rotas:
/usuarios/cadastro/: Página de cadastro de usuário.
/usuarios/login/: Página de login.
/usuarios/logout/: Logout do usuário.


### 6. Aplicativo livros
Gerencia o cadastro e manutenção dos livros.



### 6.1. Modelos (models.py)
Define o modelo Livro.


    from django.db import models

    class Livro(models.Model):
        titulo = models.CharField(max_length=255)
        autor = models.CharField(max_length=255)
        isbn = models.CharField(max_length=13, unique=True)
        disponivel = models.BooleanField(default=True)

        def __str__(self):
            return self.titulo
Campos:
titulo e autor: Informações básicas do livro.
isbn: Número único de identificação do livro.
disponivel: Indica se o livro está disponível para empréstimo.


### 6.2. Formulários (forms.py)
Define formulários para criar e editar livros.


    from django import forms
    from .models import Livro

    class LivroForm(forms.ModelForm):
        class Meta:
            model = Livro
            fields = ['titulo', 'autor', 'isbn', 'disponivel']


### 6.3. Views (views.py)
Contém as views para gerenciar livros.


    from django.shortcuts import render, redirect
    from .forms import LivroForm
    from .models import Livro

    def listar_livros(request):
        livros = Livro.objects.all()
        return render(request, 'listar_livros.html', {'livros': livros})

    def cadastrar_livro(request):
        if request.method == 'POST':
            form = LivroForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('listar_livros')
        else:
            form = LivroForm()
        return render(request, 'cadastrar_livro.html', {'form': form})
listar_livros: Exibe a lista de todos os livros.
cadastrar_livro: Permite adicionar um novo livro.


### 6.4. URLs (urls.py)
Define as rotas para o aplicativo livros.


    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.listar_livros, name='listar_livros'),
        path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    ]


### 7. Aplicativo emprestimos
Gerencia os empréstimos de livros aos usuários.



### 7.1. Modelos (models.py)
Define o modelo Emprestimo.


    from django.db import models
    from usuarios.models import Usuario
    from livros.models import Livro

    class Emprestimo(models.Model):
        usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
        livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
        data_emprestimo = models.DateField(auto_now_add=True)
        data_devolucao = models.DateField(null=True, blank=True)

        def __str__(self):
            return f"{self.livro.titulo} emprestado a {self.usuario.username}"
Relacionamentos:
usuario: Usuário que realizou o empréstimo.
livro: Livro emprestado.
Campos de Data:
data_emprestimo: Data em que o empréstimo foi realizado.
data_devolucao: Data em que o livro foi devolvido.


### 7.2. Formulários (forms.py)
Define formulários para criar e encerrar empréstimos.


    from django import forms
    from .models import Emprestimo

    class EmprestimoForm(forms.ModelForm):
        class Meta:
            model = Emprestimo
            fields = ['usuario', 'livro']


### 7.3. Views (views.py)
Contém as views para gerenciar empréstimos.


    from django.shortcuts import render, redirect
    from .forms import EmprestimoForm
    from .models import Emprestimo

    def listar_emprestimos(request):
        emprestimos = Emprestimo.objects.all()
        return render(request, 'listar_emprestimos.html', {'emprestimos': emprestimos})

    def realizar_emprestimo(request):
        if request.method == 'POST':
            form = EmprestimoForm(request.POST)
            if form.is_valid():
                emprestimo = form.save()
                emprestimo.livro.disponivel = False
                emprestimo.livro.save()
                return redirect('listar_emprestimos')
        else:
            form = EmprestimoForm()
        return render(request, 'realizar_emprestimo.html', {'form': form})
listar_emprestimos: Exibe a lista de todos os empréstimos.
realizar_emprestimo: Permite registrar um novo empréstimo e atualiza o status do livro para indisponível.


### 7.4. URLs (urls.py)
Define as rotas para o aplicativo emprestimos.


    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.listar_emprestimos, name='listar_emprestimos'),
        path('realizar/', views.realizar_emprestimo, name='realizar_emprestimo'),
    ]

### 8. Templates
Os templates são responsáveis pela apresentação visual do sistema.



### 8.1. Herança de Templates
O template base base.html define a estrutura comum a todas as páginas.


    <!-- templates/base.html -->

    {% load static %}

    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Sistema de Biblioteca - Genius Lab</title>
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    </head>
    <body>
        <header>
            <h1>Sistema de Biblioteca - Genius Lab</h1>
            <nav>
                <ul>
                    <li><a href="{% url 'index' %}">Início</a></li>
                    {% if user.is_authenticated %}
                        {% if user.tipo_usuario == 'admin' %}
                            <li><a href="{% url 'cadastro_usuario' %}">Cadastrar Usuário</a></li>
                            <li><a href="{% url 'cadastrar_livro' %}">Cadastrar Livro</a></li>
                        {% endif %}
                        <li><a href="{% url 'logout_usuario' %}">Logout</a></li>
                    {% else %}
                        <li><a href="{% url 'login_usuario' %}">Login</a></li>
                    {% endif %}
                </ul>
            </nav>
        </header>

    {% block content %}
    <!-- Conteúdo específico de cada página -->
    {% endblock %}

    <footer>
        <p>&copy; 2023 Genius Lab</p>
    </footer>
    </body>
    </html>

{% block content %}: Área onde os templates filhos inserem seu conteúdo.
{% if user.is_authenticated %}: Exibe opções no menu dependendo do status do usuário.


### 8.2. Templates Específicos
Exemplo de um template que herda de base.html:


<!-- templates/index.html -->

    {% extends 'base.html' %}

    {% block content %}
        <h2>Bem-vindo ao Sistema de Biblioteca!</h2>
        <p>Utilize o menu para navegar pelo sistema.</p>
    {% endblock %}
    {% extends 'base.html' %}: Indica que este template herda de base.html.
    {% block content %}: Define o conteúdo específico desta página.


### 9. Fluxo de Dados no Sistema
O sistema permite que usuários interajam com livros e empréstimos de forma controlada.



### 9.1. Autenticação e Autorização
Usuários Administradores:

* Podem cadastrar novos usuários.
* Podem cadastrar novos livros.
* Podem realizar e gerenciar empréstimos.
* Usuários Leitores:
* Podem visualizar livros disponíveis.
* Podem solicitar empréstimos (implementação futura).


### 9.2. Gerenciamento de Livros
Cadastro de Livros:

* Administradores podem adicionar livros ao sistema.
* Informações como título, autor e ISBN são registradas.
* Listagem de Livros:
* Todos os usuários podem visualizar os livros cadastrados.

### 9.3. Gerenciamento de Empréstimos
Realização de Empréstimos:

* Administradores podem registrar um empréstimo associando um livro a um usuário.
* Ao realizar um empréstimo, o status do livro é atualizado para indisponível.
* Listagem de Empréstimos:
* É possível visualizar todos os empréstimos realizados, com informações de datas e usuários.


### 10. Conclusão

###### Este documento detalhou a funcionalidade completa do sistema de biblioteca desenvolvido na Genius Lab. Cada componente foi explicado, desde a estrutura de arquivos até a comunicação entre os módulos. Esperamos que esta documentação facilite a compreensão do sistema e sirva como referência para futuras manutenções ou extensões.

##### Principais Conceitos Abordados:

* Arquitetura Django: Compreensão de como projetos e aplicativos são estruturados.

* Modelos: Definição de estruturas de dados usando models.py.

* Formulários: Criação de formulários com forms.py para interação com o usuário.

* Views: Lógica de processamento em views.py que manipula requisições e respostas.

* URLs: Mapeamento de rotas em urls.py para direcionar as requisições.

* Templates: Utilização de templates para renderização de páginas HTML.

* Autenticação: Implementação de um modelo de usuário customizado e gerenciamento de autenticação.

* Comunicação entre Aplicativos: Como diferentes aplicativos (usuarios, livros, emprestimos) interagem através de relacionamentos em modelos.

* Próximos Passos:

* Implementar Funcionalidades Adicionais: Como renovação de empréstimos, reservas de livros e notificações.

* Melhorias na Interface: Aprimorar o design e a usabilidade do sistema.

* Segurança: Implementar medidas de segurança adicionais para proteger os dados e as operações do sistema.

* Testes Automatizados: Desenvolver testes para garantir a confiabilidade do sistema.

