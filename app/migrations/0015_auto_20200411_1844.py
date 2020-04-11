# Generated by Django 3.0.5 on 2020-04-11 18:44

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200411_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterbase',
            name='appearance',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='archery',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='athletics',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='awareness',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='brawl',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='bureaucracy',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='charisma',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='craft',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='dexterity',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='dodge',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='integrity',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='intelligence',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='investigation',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='larceny',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='linguistics',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='lore',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='manipulation',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='martialArts',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='melee',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='occult',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='perception',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='performance',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='presence',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='resistance',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='ride',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='sail',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='socialize',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='stamina',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='stealth',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='strength',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='survival',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='thrown',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='war',
        ),
        migrations.RemoveField(
            model_name='characterbase',
            name='wits',
        ),
        migrations.AlterField(
            model_name='characterexaltlunar',
            name='attributeFavored',
            field=app.models.MultiChoiceField(blank=True, choices=[('Physical', (('STR', 'Strength'), ('DEX', 'Dexterity'), ('STA', 'Stamina'))), ('Social', (('CHA', 'Charisma'), ('MAN', 'Manipulation'), ('APP', 'Appearance'))), ('Mental', (('PER', 'Perception'), ('INT', 'Intelligence'), ('WIT', 'Wits')))], max_length=100, verbose_name='Favoured Attributes'),
        ),
        migrations.AlterField(
            model_name='charmlunar',
            name='attribute',
            field=app.models.SingleChoiceField(blank=True, choices=[('Physical', (('STR', 'Strength'), ('DEX', 'Dexterity'), ('STA', 'Stamina'))), ('Social', (('CHA', 'Charisma'), ('MAN', 'Manipulation'), ('APP', 'Appearance'))), ('Mental', (('PER', 'Perception'), ('INT', 'Intelligence'), ('WIT', 'Wits')))], max_length=100, verbose_name='Key Attribute'),
        ),
        migrations.AlterField(
            model_name='modifierattribute',
            name='attribute',
            field=app.models.SingleChoiceField(blank=True, choices=[('Physical', (('STR', 'Strength'), ('DEX', 'Dexterity'), ('STA', 'Stamina'))), ('Social', (('CHA', 'Charisma'), ('MAN', 'Manipulation'), ('APP', 'Appearance'))), ('Mental', (('PER', 'Perception'), ('INT', 'Intelligence'), ('WIT', 'Wits')))], max_length=100, verbose_name='Attribute'),
        ),
    ]
