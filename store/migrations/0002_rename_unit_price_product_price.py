# Generated by Django 4.1.3 on 2022-12-01 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='unit_price',
            new_name='price',
        ),
    ]
