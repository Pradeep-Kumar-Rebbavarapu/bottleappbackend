# Generated by Django 4.0.4 on 2022-05-20 18:48

import api.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datestamp',
            field=models.CharField(blank=True, default=api.helpers.getdate, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='timestamp',
            field=models.CharField(blank=True, default=api.helpers.gettime, max_length=225, null=True),
        ),
    ]