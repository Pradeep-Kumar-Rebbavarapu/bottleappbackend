# Generated by Django 4.0.4 on 2022-05-27 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_product_uuid_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='uuid',
        ),
    ]