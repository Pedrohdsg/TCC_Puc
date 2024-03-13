from django.contrib import admin
from apps.lista_compras.models import ListaDeCompras, ItemDeLista

class ItemDeListaInline(admin.TabularInline):
    model = ItemDeLista
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        if obj:
            return super().get_formset(request, obj, **kwargs)
        else:
            return super().get_formset(request, None, **kwargs)

class ListaDeComprasAdmin(admin.ModelAdmin):
    list_display = ('nome','id',)
    inlines = [ItemDeListaInline]
    list_display_links = ('nome','id',)
    list_per_page = 10

admin.site.register(ListaDeCompras, ListaDeComprasAdmin)

