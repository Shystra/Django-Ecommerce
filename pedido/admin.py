from django.contrib import admin
from . import models

#TODO QUANDO VISUALIZAR UM PEDIDO A GENTE JA VISUALIZA TODOS OS ITENS
class ItemPedidoInline (admin.TabularInline):
    model = models.ItemPedido
    #TODO EXIBE A QUANTIDADE DE CAMPOS
    extra = 1

class PedidoAdmin (admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]


admin.site.register (models.Pedido)
admin.site.register (models.ItemPedido)
