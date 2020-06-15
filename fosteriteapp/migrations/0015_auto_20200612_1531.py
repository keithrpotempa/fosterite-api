# Generated by Django 3.0.7 on 2020-06-12 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fosteriteapp', '0014_auto_20200612_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='adopted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='fosteriteapp.Foster'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='litter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fosteriteapp.Litter'),
        ),
        migrations.AlterField(
            model_name='litter',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='fosteriteapp.Cat'),
        ),
    ]
