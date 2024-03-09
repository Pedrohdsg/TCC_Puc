from django.contrib import admin
from apps.receita.models import Receita, ReceitaIngrediente, Ingrediente


class ReceitaIngrdienteInline(admin.TabularInline):
    model = ReceitaIngrediente
    extra = 1

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_Receita','tipo','publicada','data_receita','usuario')
    inlines = [ReceitaIngrdienteInline]
    search_fields = ('nome_Receita',)
    list_display_links = ('id', 'nome_Receita','tipo',)
    list_filter = ('tipo','usuario')
    list_editable = ('publicada',)
    list_per_page = 10
    

admin.site.register(Ingrediente)


