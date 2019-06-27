# Generated by Django 2.2.2 on 2019-06-26 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190624_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('endereco', models.CharField(max_length=200)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.CPF')),
                ('departamentos', models.ManyToManyField(blank=True, to='clientes.Departamento')),
            ],
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.AddField(
            model_name='telefone',
            name='empregado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Empregado'),
            preserve_default=False,
        ),
    ]
