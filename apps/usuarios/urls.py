from django.urls import path, include
from apps.usuarios.views import logar, cadastro, deslogar

urlpatterns = [
    path('logar/', logar, name='logar'),
    path('cadastro/', cadastro, name='cadastro'),
    path('deslogar/', deslogar, name='deslogar'),
]