# Generated by Django 4.2.7 on 2023-11-24 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestorApp', '0002_alter_encomienda_caracteristicas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='numero_bus',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='bus',
            name='placa_bus',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='encomienda',
            name='caracteristicas',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(100000)]),
        ),
    ]
