from django import forms
from apps.receita.models import Receita, ReceitaIngrediente
from django.forms.models import inlineformset_factory



class ReceitaForms(forms.ModelForm):
    class Meta:
        model = Receita
        exclude = ['publicada','ingredientes','data_receita','modo_de_preparo','usuario']
        labels= {
            'data_receita':'Data de registro',
            'usuario':'Usuário'            
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'modo_de_preparo': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }

class EditarReceitaForms(forms.ModelForm):
    class Meta:
        model = Receita
        exclude = ['publicada','ingredientes','data_receita','usuario']
        labels= {
            'data_receita':'Data de registro',
            'usuario':'Usuário'            
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'modo_de_preparo': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }

IngredienteFormSet = inlineformset_factory(Receita, ReceitaIngrediente, fields=('ingrediente', 'quantidade', 'unidade', 'categoria'), extra=1)