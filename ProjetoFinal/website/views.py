from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'website/index.html')


def contato(request):
    import pdb; pdb.set_trace()
    return render(request, 'website/contato.html')


def servicos(request):
    return render(request, 'website/servicos.html')
