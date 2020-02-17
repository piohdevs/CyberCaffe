# Generated by Django 2.2.9 on 2020-02-17 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0007_auto_20200212_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
