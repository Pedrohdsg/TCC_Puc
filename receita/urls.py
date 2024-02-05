from django.urls import path
from receita.views import index, receitas

urlpatterns = [
    path('', index, name='home'),
    path('receitas/', receitas, name='receitas'),
]