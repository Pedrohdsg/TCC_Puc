from django.shortcuts import render, get_object_or_404, redirect
from apps.receita.models import Receita, Ingrediente
from apps.receita.forms import ReceitaForms, EditarReceitaForms, IngredienteFormSet
from django.contrib import messages
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    receitas = Receita.objects.order_by('data_receita').filter(publicada=True)
    return render(request, 'receita/index.html', {"cards": receitas})

def receitas(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    massa_ingredientes = receita.receitaingrediente_set.filter(categoria='massa')
    recheio_ingredientes = receita.receitaingrediente_set.filter(categoria='recheio')
    cobertura_ingredientes = receita.receitaingrediente_set.filter(categoria='cobertura')
    generico_ingredientes = receita.receitaingrediente_set.filter(categoria='')
    return render(request, 'receita/receitas.html', {"receita": receita, 'massa_ingredientes': massa_ingredientes, 'recheio_ingredientes': recheio_ingredientes, 'cobertura_ingredientes': cobertura_ingredientes, 'generico_ingredientes':generico_ingredientes})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    receitas = Receita.objects.order_by('data_receita').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            receitas = receitas.filter(nome_Receita__icontains = nome_a_buscar)

    return render(request, "receita/index.html", {"cards": receitas})


def nova_receita(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = ReceitaForms()
    if request.method == 'POST':
        form = ReceitaForms(request.POST, request.FILES)
        if form.is_valid():
            nova_receita = form.save(commit=False)
            nova_receita.usuario = request.user
            nova_receita.save()
            form.save_m2m()
            messages.success(request, 'Nova receita adicionada!')
            return redirect('editar_receita', receita_id=nova_receita.pk)

    return render(request, 'receita/nova_receita.html', {'form': form})

def editar_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    
    if request.method == 'POST':
        form = EditarReceitaForms(request.POST, request.FILES, instance=receita)
        formset = IngredienteFormSet(request.POST, instance=receita)
        if form.is_valid() and formset.is_valid():
            novo_ingrediente_nome = request.POST.get('novo_ingrediente')
            if novo_ingrediente_nome:
                novo_ingrediente_nome, create = Ingrediente.objects.get_or_create(nome=novo_ingrediente_nome)
            formset.save()
            form.save()
            messages.success(request, 'Receita editada com sucesso!')
            return HttpResponseRedirect(request.path_info)
            
    else:
        form = EditarReceitaForms(instance=receita)
        formset = IngredienteFormSet(instance=receita)
      
    return render(request, 'receita/editar_receita.html', {'form': form, 'formset':formset, 'receita_id':receita_id})

def deletar_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    
    if receita.usuario == request.user:
        receita.publicada=False
        receita.save()
        messages.success(request, 'Receita deletada!')
        return redirect('home')
    else:
        messages.error(request, 'Usuário não tem permissão para apagar essa receita!')
        return redirect('home')


def filtro(request, tipo):
    receitas = Receita.objects.order_by('data_receita').filter(publicada=True, tipo=tipo)
    return render(request, 'receita/index.html', {"cards": receitas})