from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contatos

def index(request):
    contatos = Contatos.objects.all()
    return render(request, 'inicio/index.html', {
        'contatos':contatos,
    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contatos, id=contato_id)
    return render(request, 'inicio/ver_contato.html', {
        'contato': contato
    })