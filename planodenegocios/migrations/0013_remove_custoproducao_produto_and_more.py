# Generated by Django 5.2 on 2025-07-08 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planodenegocios', '0012_alter_custoproducao_embalagem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custoproducao',
            name='produto',
        ),
        migrations.AddField(
            model_name='custoproducao',
            name='custo_unitario',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='custoproducao',
            name='produto_servico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='custos', to='planodenegocios.produtoservico'),
            preserve_default=False,
        ),
    ]
