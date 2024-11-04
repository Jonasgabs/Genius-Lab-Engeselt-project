from django.contrib import admin
from django.urls import path, include

urlpatterns = [ # Inclui as rotas definidas em core
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
