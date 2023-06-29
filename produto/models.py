from django.db import models
from django.utils.text import slugify

from utils import utils, resize_image

# Create your models here.
class Produto(models.Model):
  nome = models.CharField(max_length=255)
  descricao_curta = models.TextField(max_length=255)
  descricao_longa = models.TextField()
  imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True)
  slug = models. SlugField(unique=True, blank=True, null=True)
  preco_marketing = models.FloatField()
  preco_marketing_promocional = models.FloatField(default=0)
  tipo = models.CharField(
    default='S',
    max_length=1,
    choices=(
      ('S', 'Simples'),
      ('V', 'Variação')
    )
  )

  def get_preco_formatado(self):
    return utils.formata_preco(self.preco_marketing)
  get_preco_formatado.short_description = 'Preço'

  def get_preco_promocional_formatado(self):
    return utils.formata_preco(self.preco_marketing_promocional)
  get_preco_promocional_formatado.short_description = 'Preço Promo.'

  def save(self, *args, **kwargs):
    if not self.slug:
      slug = f'{slugify(self.nome)}'
      self.slug = slug

    super().save(*args, **kwargs)

    if self.imagem:
      resize_image.resize_image(self.imagem)

  def __str__(self):
    return self.nome


class Variacao(models.Model):
  class Meta:
    verbose_name = 'Variação'
    verbose_name_plural = 'Variações'

  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  nome = models.CharField(max_length=255)
  preco = models.FloatField()
  preco_promocional = models.FloatField(default=0)
  estoque = models.PositiveIntegerField(default=1)

  def __str__(self):
    return self.nome
