from django.shortcuts import render
from .models import Contatos

def index(request):
    contatos = Contatos.objects.all()
    return render(request, 'inicio/index.html', {
        'contatos':contatos,
    })
