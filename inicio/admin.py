from django.contrib import admin
from .models import Contatos, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    list_filter = ('data_criacao',)
    list_display_links = ('id', 'nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'telefone')

admin.site.register(Categoria)
admin.site.register(Contatos, ContatoAdmin)
