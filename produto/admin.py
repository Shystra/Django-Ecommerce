from django.contrib import admin
from . import models



#TODO Para criar um inline no painel (tabela)
class VariacaoInline (admin.TabularInline):
    model = models.Variacao
    #TODO Exibe a quantidade de campos
    extra = 1

class ProdutoAdmin (admin.ModelAdmin):
    #TODO PARA PODER APARECER
    list_display = ['nome', 'descricao_curta',
               'get_preco_formatado', 'get_preco_promocional_formatado']
    #TODO QUANDO ENTRAR NO PRODUTO, MOSTRARÁ QUANTOS FILHOS DO PRODUTO ELE TEM
    inlines = [
        VariacaoInline
    ]


admin.site.register (models.Produto, ProdutoAdmin)
admin.site.register (models.Variacao)
