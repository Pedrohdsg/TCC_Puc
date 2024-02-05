from django.shortcuts import render

def index(request):
    return render(request, 'receita/index.html')

def receitas(request):
    return render(request, 'receita/receitas.html')