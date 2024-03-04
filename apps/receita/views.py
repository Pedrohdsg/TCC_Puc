from django.shortcuts import render, get_object_or_404, redirect
from apps.receita.models import Receita, Ingrediente
from apps.receita.forms import ReceitaForms, IngredienteFormSet
from django.contrib import messages



def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    receitas = Receita.objects.order_by('data_receita').filter(publicada=True)
    return render(request, 'receita/index.html', {"cards": receitas})

def receitas(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'receita/receitas.html', {"receita": receita})

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
    
    form = ReceitaForms
    if request.method == 'POST':
        form = ReceitaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova receita adicionada!')
            return redirect('home')

    return render(request, 'receita/nova_receita.html', {'form': form})

def editar_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    if request.method == 'POST':
        form = ReceitaForms(request.POST, request.FILES, instance=receita)
        formset = IngredienteFormSet(request.POST, instance=receita)
        if form.is_valid() and formset.is_valid():
            novo_ingrediente_nome = request.POST.get('novo_ingrediente')
            if novo_ingrediente_nome:
                novo_ingrediente_nome, create = Ingrediente.objects.get_or_create(nome=novo_ingrediente_nome)
            formset.save()
            form.save()
            messages.success(request, 'Receita editada com sucesso!')
            return render(request, 'receita/editar_receita.html', {'form': form, 'formset':formset, 'receita_id':receita_id})
            # return render(request, 'receita/receitas.html', {"receita": receita})
            # return redirect('home')
    else:
        form = ReceitaForms(instance=receita)
        formset = IngredienteFormSet(instance=receita)

        

    return render(request, 'receita/editar_receita.html', {'form': form, 'formset':formset, 'receita_id':receita_id})

def deletar_receita(request, receita_id):
    receita = Receita.objects.get(id=receita_id)
    receita.delete()
    messages.success(request, 'Receita deletada!')

    return redirect('home')

def filtro(request, tipo):
    receitas = Receita.objects.order_by('data_receita').filter(publicada=True, tipo=tipo)
    return render(request, 'receita/index.html', {"cards": receitas})