from django.contrib import admin
from .models import Contatos, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    #list_filter = ('data_criacao',)
    list_display_links = ('id', 'nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contatos, ContatoAdmin)
