# Generated by Django 5.2 on 2025-07-20 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planodenegocios', '0021_gestaoqualidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnaliseRiscos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Análise de Riscos')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
