from django.shortcuts import render, get_object_or_404, redirect
from apps.lista_compras.models import ListaDeCompras, ItemDeLista
from django.contrib import messages
from django.http import HttpResponseRedirect
from apps.lista_compras.forms import ListaDeComprasForm, AdicionarItemForm, DeletarItemForm

def lista_compras(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('logar')

    lista_compras = ListaDeCompras.objects.all()
    return render(request, 'lista_compras/listas.html', {"cards": lista_compras})

def nova_lista_compras(request):
    if request.method == 'POST':
        form = ListaDeComprasForm(request.POST)
        if form.is_valid():
            lista_de_compras = form.save(commit=False)
            lista_de_compras.usuario = request.user
            lista_de_compras.save()
            messages.success(request, 'Nova lista adicionada!')
            return redirect('editar_lista_compras', lista_id=lista_de_compras.id)
    else:
        form = ListaDeComprasForm()
    
    return render(request, 'lista_compras/nova_lista.html', {'form': form})

def editar_lista_compras(request, lista_id):
    lista = get_object_or_404(ListaDeCompras, id=lista_id)
    adicionar_form = AdicionarItemForm()
    deletar_form = DeletarItemForm()
    if lista.usuario == request.user:
        if request.method == 'POST':
            if 'adicionar' in request.POST:
                adicionar_form = AdicionarItemForm(request.POST)
                if adicionar_form.is_valid():
                    novo_item = adicionar_form.save(commit=False)
                    novo_item.lista = lista
                    novo_item.save()
                messages.success(request, 'Lista editada com sucesso!')
                return redirect('editar_lista_compras', lista_id=lista_id)
            elif 'deletar' in request.POST:
                deletar_form = DeletarItemForm(request.POST)
                if deletar_form.is_valid():
                    item_id = deletar_form.cleaned_data['item_id']
                    item = get_object_or_404(ItemDeLista, id=item_id, lista=lista)
                    item.delete()
                    return redirect('editar_lista_compras', lista_id=lista_id)
    else: 
        messages.error(request, 'Usuário não tem permissão para editar essa lista!')
        return redirect('home')
    return render(request, 'lista_compras/lista_compras.html', {
        'lista': lista,
        'adicionar_form': adicionar_form,
        'deletar_form': deletar_form
    })


def deletar_lista_compras(request, lista_id):
    lista= ListaDeCompras.objects.get(id=lista_id)
    if lista.usuario == request.user:
        lista.delete()
        messages.success(request, 'Lista deletada!')
        return redirect('lista_compras')
    else:
        messages.error(request, 'Usuário não tem permissão para apagar essa lista!')
        return render('lista_compras')