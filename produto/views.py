from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ListaProdutos (View):
    model = models.Produto
    template_name = 'produto/lista.html'








class DetalheProduto (View):
    def get (self, *args, **kwargs):
        return HttpResponse ('Detalhe Produto')

class AdicionarAoCarrinho (View):
    def get (self, *args, **kwargs):
        return HttpResponse ('Adicionar carrinho')

class RemoverDoCarrinho (View):
    def get (self, *args, **kwargs):
        return HttpResponse ('Remover Carrinho')


class Carrinho (View):
    def get (self, *args, **kwargs):
        return HttpResponse ('Carrinho')


class Finalizar (View):
    def get (self, *args, **kwargs):
        return HttpResponse ('Finalizar')

