# Generated by Django 3.0.7 on 2020-06-11 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fosteriteapp', '0008_auto_20200611_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='adopted_id',
            new_name='adopted',
        ),
        migrations.RenameField(
            model_name='cat',
            old_name='breed_id',
            new_name='breed',
        ),
    ]
