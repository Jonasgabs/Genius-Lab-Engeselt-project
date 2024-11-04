# DESAFIO TÉCNICO - ESTÁGIO PYTHON/DJANGO

## Descrição do Sistema

---


##### *O Sistema de Controle de Biblioteca para a Genius Labrepresenta uma inovação significativa no gerenciamento debibliotecas educacionais. Com uma interface amigável efuncionalidades robustas, a plataforma digitaliza e simplificaprocessos que tradicionalmente consomem tempo e recursos.Administradores têm à disposição ferramentas avançadas paracatalogar novos livros, acompanhar o status dos empréstimos egerar relatórios que oferecem insights sobre a circulação dosmateriais. Isso não só melhora a eficiência operacional, mastambém permite decisões informadas para a expansão doacervo. Por outro lado, os usuários desfrutam de umaexperiência otimizada, com acesso rápido a informações sobredisponibilidade de livros e um histórico de empréstimos quefacilita a gestão pessoal de suas leituras. Essa solução nãoapenas melhora o acesso aos recursos educacionais, mastambém promove um ambiente de aprendizagem maisorganizado e eficiente.*

---

## o arquivo requirementes foi gerado usando : 
    pip freeze > requirements.txt

*para rodar o projeto baixe todos os requirimentos do sistemas com :*

    pip install -r requirements.txt

*em seguida digite*

    python manage.py runserver

---

## assim está estruturado o sistema :

    Projeto/
    ├── biblioteca_genius_lab/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │
    ├── core/                     # Aplicação  para funcionalidades essenciais
    │   ├── migrations/
    │   ├── templates/
    │   │   ├── home.html
    │   │   ├── login.html
    │   │   └── lista_livros.html
    │   ├── __init__.py
    │   ├── models.py             # Modelos para Usuário, Livro e Empréstimo
    │   ├── views.py              # Views para cada funcionalidade principal
    │   ├── urls.py               # URLs específicas da aplicação
    │   └── forms.py              # Formulários para login e empréstimos
    │
    ├── manage.py
    └── README.md



