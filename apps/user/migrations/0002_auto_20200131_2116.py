# Generated by Django 2.2.9 on 2020-01-31 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name'], 'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefono'),
        ),
    ]
