# Generated by Django 2.2.9 on 2020-02-07 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_advertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='name',
            field=models.CharField(default='name', max_length=60),
        ),
    ]