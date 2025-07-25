# Generated by Django 5.2 on 2025-07-16 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ampliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('depreciacao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('credito', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='CustoProducao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=255)),
                ('frete', models.DecimalField(decimal_places=2, max_digits=10)),
                ('embalagem', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DespesaMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.PositiveSmallIntegerField()),
                ('tipo', models.CharField(choices=[('alimentacao', 'Alimentação'), ('transporte', 'Transporte')], max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EncargoGlobal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentual', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
                ('quantidade', models.PositiveIntegerField()),
                ('salario_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('descricao', models.CharField(max_length=200)),
                ('quantidade', models.PositiveIntegerField()),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('depreciacao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('credito', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('servico', 'Serviço'), ('terceiros', 'Produto de terceiros'), ('fabricacao', 'Fabricação própria')], max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('unidade_venda', models.CharField(max_length=20)),
                ('margem_lucro', models.DecimalField(decimal_places=2, max_digits=5)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_varia', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Encargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentual', models.DecimalField(decimal_places=2, max_digits=5)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planodenegocios.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('alimentacao', 'Alimentação'), ('transporte', 'Transporte')], max_length=20)),
                ('mes', models.PositiveSmallIntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planodenegocios.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='SalarioMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.PositiveSmallIntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planodenegocios.funcionario')),
            ],
        ),
    ]
