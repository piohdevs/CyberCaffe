# Generated by Django 2.2.9 on 2020-02-07 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_advertise_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertise',
            old_name='type_image',
            new_name='type_advertise',
        ),
    ]
