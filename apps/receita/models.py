from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


    
class Ingrediente(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.nome
    

class Receita(models.Model):
    
    TIPO_RECEITA = [
        ("PETISCOS","Petiscos"),
        ("DOCES","Doces"),
        ("PRATOS","Pratos"),
        ("ENTRADAS","Entradas"),
    ]

    nome_Receita = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.CharField(max_length=10,choices=TIPO_RECEITA, default='')
    ingredientes = models.ManyToManyField(Ingrediente, through="ReceitaIngrediente")
    modo_de_preparo = models.TextField()
    publicada = models.BooleanField(default=True)
    data_receita = models.DateTimeField(default=datetime.now, blank=False)
    foto=models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        return f"Receita: {self.nome_Receita} - {self.tipo}"
    
class ReceitaIngrediente(models.Model):

    UNIDADE_MEDIDA = {
        "g":"gramas",
        "kg":"quilos",
        "ml":"mililitros",
        "l":"litros",
        "colher(es) chá":"colheres chá",
        "colher(es) sopa":"colheres sopa",
        "un":"unidades",
        "xícara(s)":"xícaras",
        "pitada":"pitada",
        "lata(s)":"lata",
        "à gosto": "à gosto"
    }
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=4, decimal_places=1)
    unidade = models.CharField(max_length=15, choices=UNIDADE_MEDIDA)
    

    def __str__(self):
        return f"{str(self.receita)} - {self.quantidade} {self.unidade}"
    
