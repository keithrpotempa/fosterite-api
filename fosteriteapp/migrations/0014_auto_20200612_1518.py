# Generated by Django 3.0.7 on 2020-06-12 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fosteriteapp', '0013_auto_20200612_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='bonded_pair_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fosteriteapp.Cat'),
        ),
    ]
