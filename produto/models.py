from django.db import models
import os
from django.conf import settings
from PIL import Image
from django.utils.text import slugify
from utils import utils

class Produto(models.Model):
    nome = models.CharField (max_length = 255)

    descricao_curta = models.TextField (max_length = 255)
    descricao_longa = models.TextField ()
    imagem = models.ImageField(
        upload_to = 'produto_imagens/%Y/%m/', blank = True, null = True
    )
    slug = models.SlugField (unique = True, blank = True, null = True )
    preco_marketing = models.FloatField (verbose_name = 'Preço')
    preco_marketing_promocional = models.FloatField (default = 0, verbose_name = 'Preço Promo.')

    #TODO Para criar o botao de variação segue modelo abaixo
    tipo = models.CharField ( 
        default = 'V',
        max_length = 1, 
        choices = (
        
            ('V', 'Variável'),
            ('S', 'Simples'),
        ) 
    )

    def get_preco_formatado (self):   
        return utils.formata_preco (self.preco_marketing)
    
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado (self):
        return utils.formata_preco (self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = 'Preço Promo.'


    #TODO Adiciona caminho na Pasta
    @staticmethod
    def resize_image (img, new_width = 800):
        img_full_path = os.path.join (settings.MEDIA_ROOT, img.name)

        #TODO PARA PEGAR A IMAGEM COM PILLOW (LARGURA E ALTURA)
        img_pil = Image.open (img_full_path)
        original_width, original_height = img_pil.size
        
        if original_width <= new_width:
            print ('Retornando, largura original menor que a nova largura')
            img_pil.close ()
            return
        """
        REGRA DE 3 PARA OBTER IMAGEM
        largura / altura
        nova_largura / nova altura???
        """ #TODO REGRA DE 3
        new_height = round ((new_width *original_height) / original_width)

        #TODO Reduz a imagem 
        new_img = img_pil.resize ((new_width, new_height), Image.LANCZOS)
        new_img.save (
            optimize = True,
            quality = 50
        )
        print ('Imagem foi redimensionada.')

    #TODO SALVA IMAGEM E ENVIA
    def save (self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save (*args, **kwargs)

    #TODO SE A IMAGEM FOR ENVIADA ELE REDIMENSIONA 
        max_image_size = 800
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)


    #TODO Retorna o nome do produto criado
    def __str__ (self):
        return self.nome
    

class Variacao (models.Model):
    #TODO Quando deletar o produto todas as variações irão juntas
    produto = models.ForeignKey (Produto, on_delete = models.CASCADE)
    # --------------------------------------------------------------- #
    nome = models.CharField (max_length = 50, blank = True, null = True)
    preco = models.FloatField ()
    preco_promocional = models.FloatField (default = 0)
    estoque = models.PositiveIntegerField (default = 1)

#TODO Exibe o nome da variação ou produto
    def __str__(self):
        return self.nome or self.produto.nome

#TODO AJUSTA A NOMENCLATURA NO PAINEL
    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = "Variações"