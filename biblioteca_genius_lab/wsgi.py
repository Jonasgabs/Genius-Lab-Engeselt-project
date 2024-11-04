import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_genius_lab.settings') # Cria a  WSGI para produção
application = get_wsgi_application()

