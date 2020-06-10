# Generated by Django 3.0.7 on 2020-06-10 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fosteriteapp', '0004_litter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FosterRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fosteriteapp.Cat')),
                ('foster', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fosteriteapp.Foster')),
            ],
        ),
        migrations.DeleteModel(
            name='Litter',
        ),
    ]