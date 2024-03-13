from django.db import models
from django.contrib.auth.models import User

class ListaDeCompras(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class ItemDeLista(models.Model):
    MEDIDA = {
        "g":"gramas",
        "kg":"quilos",
        "l":"litros",
        "un":"unidades",
        "lata(s)":"latas",
        "un":"unidades",
        "dz":"dúzias",
        "pc":"pacotes",
        "cx":"caixas"
    }

    lista = models.ForeignKey(ListaDeCompras, on_delete=models.CASCADE, default='')
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)
    medida = models.CharField(choices=MEDIDA, max_length=20, default="un")
    comprado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome