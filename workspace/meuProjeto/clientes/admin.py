from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento

class EmpregadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos', )
    search_fields = ('id', 'nome', 'email', 'departamentos__nome')



admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)