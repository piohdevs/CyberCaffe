# Generated by Django 2.2.9 on 2020-02-01 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200131_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expend',
            options={'verbose_name': 'Historial', 'verbose_name_plural': 'Historiales de gastos'},
        ),
        migrations.AlterField(
            model_name='user',
            name='register',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
