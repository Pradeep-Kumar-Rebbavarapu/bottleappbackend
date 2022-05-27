# Generated by Django 4.0.4 on 2022-05-27 11:28

import api.helpers
import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('desc', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('image', models.FileField(upload_to=api.models.upload)),
                ('datestamp', models.CharField(blank=True, default=api.helpers.getdate, max_length=225, null=True)),
                ('timestamp', models.CharField(blank=True, default=api.helpers.gettime, max_length=225, null=True)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('Total_Price', models.IntegerField(blank=True, default=None, null=True)),
                ('product_title', models.CharField(blank=True, default=None, max_length=225, null=True)),
                ('product_image', models.URLField(default=None)),
                ('datestamp', models.CharField(blank=True, default=api.helpers.getdate, max_length=225, null=True)),
                ('timestamp', models.CharField(blank=True, default=api.helpers.gettime, max_length=225, null=True)),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
