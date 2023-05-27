from django.contrib import admin
from .models import Locacao, Filme, Categoria, Cliente

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'categoria')

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'filmes_str', 'clientes_str')

    def filmes_str(self, obj):
        return obj.filmes_str()

    def clientes_str(self, obj):
        return obj.clientes_str()

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Locacao, LocacaoAdmin)

#PAREI NO PASSO 4 - Cadastrei os dados no 'admin'