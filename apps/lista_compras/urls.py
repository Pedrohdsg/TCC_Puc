from django.urls import path
from apps.lista_compras.views import lista_compras, nova_lista_compras, editar_lista_compras, deletar_lista_compras



urlpatterns = [
    path('lista-compras', lista_compras, name='lista_compras'),
    path('nova-lista-compras',nova_lista_compras, name='nova_lista_compras'),
    path('editar-lista-compras/<int:lista_id>', editar_lista_compras, name='editar_lista_compras'),
    path('deletar-lista-compras/<int:lista_id>',deletar_lista_compras, name='deletar_lista_compras'),  
]