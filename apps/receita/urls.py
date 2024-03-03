from django.urls import path
from apps.receita.views import index, receitas, buscar, nova_receita, editar_receita, deletar_receita, filtro

urlpatterns = [
    path('', index, name='home'),
    path('receitas/<int:receita_id>', receitas, name='receitas'),
    path('buscar',buscar, name='buscar'),
    path('nova-receita',nova_receita, name='nova_receita'),
    path('editar-receita/<int:receita_id>', editar_receita, name='editar_receita'),
    path('deletar-receita/<int:receita_id>',deletar_receita, name='deletar_receita'),
    path('filtro/<str:tipo>',filtro, name='filtro'),    
]