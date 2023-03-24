from django.db import models
import os
from django.conf import settings
from PIL import Image

class Produto(models.Model):
    nome = models.CharField (max_length = 255)

    descricao_cruta = models.TextField (max_length = 255)
    descricao_longa = models.TextField ()
    imagem = models.ImageField(
        upload_to = 'produto_imagens/%Y/%m/', blank = True, null = True
    )
    slug = models.SlugField (unique = True)
    preco_marketing = models.FloatField (default = 0)
    preco_marketing_promocional = models.FloatField (default = 0)

    #TODO Para criar o botao de variação segue modelo abaixo
    tipo = models.CharField ( 
        default = 'V',
        max_length = 1, 
        choices = (
        
            ('V', 'Variação'),
            ('S', 'Simples'),
        ) 
    )

    @staticmethod
    def resize_image (img, new_width = 800):
        img_full_path = os.path.join (settings.MEDIA_ROOT, img.name)
        print(img_full_path)

    #TODO SALVA IMAGEM E ENVIA
    def save (self, *args, **kwargs):
        super().save (*args, **kwargs)

    #TODO SE A IMAGEM FOR ENVIADA ELE REDIMENCIONA 
        max_image_size = 800
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)


    #TODO Retorna o nome do produto criado
    def __str__ (self):
        return self.nome
    