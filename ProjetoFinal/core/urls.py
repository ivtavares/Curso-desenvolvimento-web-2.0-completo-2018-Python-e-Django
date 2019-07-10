from django.urls import include, path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    mov_rotativo_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    mov_rotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    mov_rotativo_delete,
    mensalista_delete,
    movmensalista_delete
    )


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoas-update/<int:id>', pessoa_update, name='core_pessoa_update'),
    path('pessoas-delete/<int:id>', pessoa_delete, name='core_pessoa_delete'),
    path('veiculo/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculos-update/<int:id>',veiculo_update, name='core_veiculo_update'),
    path('veiculos-delete/<int:id>',veiculo_delete, name='core_veiculo_delete'),
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/', mov_rotativo_novo, name='core_movrotativo_novo'),
    path('mov-rot-update/<int:id>', mov_rotativo_update, name='core_movrotativo_update'),
    path('mov-rot-delete/<int:id>', mov_rotativo_delete, name='core_movrotativo_delete'),
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<int:id>', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<int:id>', mensalista_delete, name='core_mensalista_delete'),
    path('mov-mensal', lista_movmensalistas, name='core_lista_movpessoas'),
    path('mov-mensal-novo/', movmensalista_novo, name='core_movpessoas_novo'),
    path('mov-mensal-update/<int:id>', movmensalista_update, name='core_movpessoas_update'),
    path('mov-mensal-delete/<int:id>', movmensalista_delete, name='core_movpessoas_delete')
]
