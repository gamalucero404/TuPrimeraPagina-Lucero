# Generated by Django 5.0.2 on 2024-02-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_tiendas_rename_entregable_descuentos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descuentos',
            name='entregado',
        ),
        migrations.RemoveField(
            model_name='descuentos',
            name='fecha_entrega',
        ),
        migrations.RemoveField(
            model_name='descuentos',
            name='nombre',
        ),
        migrations.AddField(
            model_name='descuentos',
            name='Tiendas',
            field=models.CharField(default='N/A', max_length=40),
        ),
        migrations.AddField(
            model_name='descuentos',
            name='productos_desc',
            field=models.CharField(default='N/A', max_length=40),
        ),
        migrations.AlterField(
            model_name='tiendas',
            name='tienda',
            field=models.CharField(max_length=40),
        ),
    ]
