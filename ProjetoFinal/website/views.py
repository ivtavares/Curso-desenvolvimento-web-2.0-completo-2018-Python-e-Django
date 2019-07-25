from django.shortcuts import render
from .models import Contato


# Create your views here.
def home(request):
    return render(request, 'website/index.html')


def contato(request):
    mensagem = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['email'] = request.POST.get('email')
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['endereco'] = request.POST.get('endereco')
            contato['mensagem'] = request.POST.get('mensagem')
            contato['receber_noticias'] = (
                True if request.POST.get('receber_noticias') == 'on' else 'False')
            Contato.objects .create(**contato)
        except Exception as e:
            mensagem = str(e)
        else:
            mensagem = 'Contato realizado com sucesso'
    return render(request, 'website/contato.html', {'mensagem': mensagem})


    


def servicos(request):
    return render(request, 'website/servicos.html')
