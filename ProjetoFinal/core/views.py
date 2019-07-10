from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
    )

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm
)


# Create your views here.


def home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'base.html',context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})
    
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update (request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else: 
        return render(request, 'core/update_veiculo.html', data)


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rot': mov_rot, 'form' : form}
    return render(request, 'core/lista_movrotativos.html', data)

def mov_rotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def mov_rotativo_update(request, id):
    data = {}
    movRotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance = movRotativo)
    data['movRotativo'] = movRotativo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect ('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)


def mov_rotativo_delete(request, id):
    movRotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movRotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movRotativo})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def mensalista_update(request, id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance = mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)        
 

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': mensalista})


def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas,  'form': form}
    return render(request, 'core/lista_mov_mensalistas.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movpessoas')


def movmensalista_update(request, id):
    data = {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance = movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movpessoas')
    else:
        return render(request, 'core/update_mov_mensalista.html', data)


def movmensalista_delete(request, id):
    movmensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core_lista_movpessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': movmensalista})