# Generated by Django 5.0.1 on 2024-03-12 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_compras', '0002_itemdelista_ingredientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdelista',
            name='ingredientes',
        ),
        migrations.AddField(
            model_name='itemdelista',
            name='lista',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lista_compras.listadecompras'),
        ),
    ]