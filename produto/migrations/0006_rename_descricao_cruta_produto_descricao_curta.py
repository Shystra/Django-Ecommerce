# Generated by Django 4.1.7 on 2023-03-24 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_alter_produto_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='descricao_cruta',
            new_name='descricao_curta',
        ),
    ]
