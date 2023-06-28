from django.contrib import admin

from produto.models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
  model = Variacao
  extra = 1


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = 'id', 'nome', 'preco_marketing', 'preco_marketing_promocional'
  list_display_links = 'nome',
  search_fields = 'id', 'name', 'preco_marketing',
  list_per_page = 10
  ordering = '-id',
  prepopulated_fields = {
    'slug': ('nome',),
  }
  inlines = VariacaoInline,

