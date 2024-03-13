from django import forms
from apps.lista_compras.models import ListaDeCompras, ItemDeLista
from django.forms.models import inlineformset_factory

class ItemDeListaForm(forms.ModelForm):
    class Meta:
        model = ItemDeLista
        fields = ['nome', 'quantidade', 'medida', 'comprado']
        labels = {
            'nome': 'Nome do Item',
            'quantidade': 'Quantidade',
            'comprado': 'Comprado',
        }

class ListaDeComprasForm(forms.ModelForm):
    class Meta:
        model = ListaDeCompras
        fields = ['nome']

class AdicionarItemForm(forms.ModelForm):
    class Meta:
        model = ItemDeLista
        fields = ['nome', 'quantidade', 'medida', 'comprado']

class DeletarItemForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput())