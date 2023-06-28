from django.db import models
from utils.resize_image import resize_image

# Create your models here.
class Produto(models.Model):
  nome = models.CharField(max_length=255)
  descricao_curta = models.TextField(max_length=255)
  descricao_longa = models.TextField()
  imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True)
  slug = models. SlugField(unique=True)
  preco_marketing = models.FloatField()
  preco_marketing_promocional = models.FloatField(blank=True, null=True)
  tipo = models.CharField(
    default='S',
    max_length=1,
    choices=(
      ('S', 'Simples'),
      ('V', 'Variação')
    )
  )

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.imagem:
      resize_image(self.imagem)

  def __str__(self):
    return self.nome


class Variacao(models.Model):
  class Meta:
    verbose_name = 'Variação'
    verbose_name_plural = 'Variações'

  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  nome = models.CharField(max_length=255)
  preco = models.FloatField()
  preco_promocional = models.FloatField(blank=True, null=True)
  estoque = models.PositiveIntegerField(default=1)

  def __str__(self):
    return self.nome
