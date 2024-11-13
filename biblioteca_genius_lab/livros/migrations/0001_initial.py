# Generated by Django 4.2.16 on 2024-11-06 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('autor', models.CharField(max_length=200, verbose_name='Autor')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('editora', models.CharField(max_length=200, verbose_name='Editora')),
                ('ano_publicacao', models.PositiveIntegerField(verbose_name='Ano de Publicação')),
                ('genero', models.CharField(choices=[('ficcao', 'Ficção'), ('nao-ficcao', 'Não-Ficção'), ('romance', 'Romance'), ('ciencia', 'Ciência')], max_length=50, verbose_name='Gênero')),
                ('quantidade_total', models.PositiveIntegerField(verbose_name='Quantidade Total')),
                ('quantidade_disponivel', models.PositiveIntegerField(default=0, verbose_name='Quantidade Disponível')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
    ]
