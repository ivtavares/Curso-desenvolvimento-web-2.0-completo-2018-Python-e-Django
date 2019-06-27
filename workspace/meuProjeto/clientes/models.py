from django.db import models

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    empregado = models.ForeignKey('Empregado', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao + ' - ' + self.numero    

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    data_exp = models.DateTimeField()

    
    def __str__(self):
        return self.numero

class Empregado(models.Model):
    nome  = models.CharField(max_length=70, null= False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email =  models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete = models.CASCADE, blank=True, null=True)
    departamentos = models.ManyToManyField(Departamento, blank=True)
    foto = models.ImageField(upload_to='cliente_fotos')
    
    def __str__(self):
        return self.nome

