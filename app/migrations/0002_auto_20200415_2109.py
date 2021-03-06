# Generated by Django 3.0.5 on 2020-04-15 21:09

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charmlunarshape',
            name='shapeType',
            field=app.models.SingleChoiceField(blank=True, choices=[('Human', 'Human'), ('Animal', 'Animal')], max_length=100, verbose_name='Shape Type'),
        ),
        migrations.AddField(
            model_name='charmlunarshape',
            name='size',
            field=app.models.SingleChoiceField(blank=True, choices=[('Normal', 'Normal')], max_length=100, verbose_name='Size'),
        ),
    ]
