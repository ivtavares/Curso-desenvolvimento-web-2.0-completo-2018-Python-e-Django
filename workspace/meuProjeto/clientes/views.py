from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clientes(request): 
    return HttpResponse('Maria, Jose e João')

def cliente_detalhe(request, id):
    return HttpResponse('Cliente Detalhe '+str(id))

def cliente_por_nome(request, nome):
    return HttpResponse('Ola {}'.format(nome))