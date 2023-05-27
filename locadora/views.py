from django.shortcuts import render
from django.http import HttpResponse
from .models import Locacao, Filme

# Create your views here.
def index(request):
    context={'nome':'Danilo Pinto Maia Sinhá',
             'info':'Esta é uma aplicação de locadora de filmes. Os modelos do sistema são: Categoria, Filme, Cliente e Locacao. Os relacionamentos entre os modelos estão definidos assim: um filme pertence a uma categoria; uma locação possui vários filmes e clientes, que pode estar associado a várias locações.'}
    return render(request, 'locadora/index.html', context)

def lista_locacao(request):
    locacao = Locacao.objects.all()
    context = {'locacao':locacao}
    return render(request, 'locadora/locacao.html', context)

def lista_filmes(request):
    filmes = Filme.objects.all()
    context = {'filmes': filmes}
    return render(request, 'locadora/filmes.html', context)