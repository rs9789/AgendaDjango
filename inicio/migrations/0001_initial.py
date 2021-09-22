# Generated by Django 3.2.7 on 2021-09-22 13:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(blank=True, max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('data_criacao', models.DateTimeField(default=datetime.datetime(2021, 9, 22, 13, 14, 12, 653337, tzinfo=utc))),
                ('descricao', models.TextField(blank=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inicio.categoria')),
            ],
        ),
    ]