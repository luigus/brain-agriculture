from dataclasses import field

from django.contrib import admin

from .models import ProdutorRural, Cultura


class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('nome_produtor', 'nome_fazenda', 'cidade', 'estado', 'area_total')
    search_fields = ('nome_produtor', 'nome_fazenda', 'cidade')
    list_filter = ('estado',)
    filter_horizontal = ('culturas_plantadas',)
    fieldsets = (
        ('Informações do Produtor', {
            'fields': ('cpf', 'cnpj', 'nome_produtor', 'nome_fazenda')
        }),
        ('Localização', {
            'fields': ('cidade', 'estado')
        }),
        ('Áreas', {
            'fields': ('area_total', 'area_agricultavel', 'area_vegetacao')
        }),
        ('Culturas', {
            'fields': ('culturas_plantadas',)
        }),
    )


class CulturaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(ProdutorRural, ProdutorRuralAdmin)
admin.site.register(Cultura, CulturaAdmin)
