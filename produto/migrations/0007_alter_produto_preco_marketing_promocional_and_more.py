# Generated by Django 4.2.2 on 2023-06-29 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco_promocional',
            field=models.FloatField(default=0),
        ),
    ]
