from django.contrib import admin
from .models import Receita

# Register your models here.
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'date_receita', 'nome_receita', 'categoria', 'tempo_de_preparo', 'publicado') #quais campos vão aparecer
    list_display_links = ('id', 'nome_receita') # definir quais campos são links
    search_fields = ('nome_receita',) # define camlpos de busca
    list_filter = ('categoria',) # define filtros de busca
    list_editable = ('publicado',) # coloca o campo como editavel
    list_per_page = 5 # define quantos registros aparecerão por página

admin.site.register(Receita, ListandoReceitas)