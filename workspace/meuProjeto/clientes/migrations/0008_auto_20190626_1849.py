# Generated by Django 2.2.2 on 2019-06-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_empregado_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='foto',
            field=models.ImageField(upload_to='cliente_fotos'),
        ),
    ]