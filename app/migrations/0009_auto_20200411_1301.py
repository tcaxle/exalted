# Generated by Django 3.0.5 on 2020-04-11 13:01

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200411_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemweaponmelee',
            name='category',
            field=app.models.SingleChoiceField(blank=True, choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], max_length=100, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='itemweaponmelee',
            name='tags',
            field=app.models.MultiChoiceField(blank=True, choices=[('General', (('ONE HANDED', 'One Handed'), ('TWO HANDED', 'Two Handed'), ('BASHING', 'Bashing'), ('CONCEALABLE', 'Concealable'), ('LETHAL', 'Lethal'), ('MOUNTED', 'Mounted'), ('PIERCING', 'Piercing'), ('SPECIAL', 'Special'))), ('Melee', (('MELEE', 'Melee'), ('BALANCED', 'Balanced'), ('BRAWL', 'Brawl'), ('CHOPPING', 'Chopping'), ('DISARMING', 'Disarming'), ('FLEXIBLE', 'Flexible'), ('IMPROVISED', 'Improvised'), ('GRAPPLING', 'Grappling'), ('MARTIAL ARTS', 'Martial Arts'), ('NATURAL', 'Natural'), ('REACHING', 'Reaching'), ('SHIELD', 'Shield'), ('SMASHING', 'Smashing'), ('WORN', 'Worn'))), ('Thrown', (('THROWN', 'Occult'), ('CUTTING', 'Cutting'), ('POISONABLE', 'Poisonable'), ('SUBTLE', 'Subtle'))), ('Archery', (('ARCHERY', 'Archery'), ('CROSSBOW', 'Crossbow'), ('FLAME', 'Flame'), ('POWERFUL', 'Powerful'), ('SLOW', 'Slow')))], max_length=100, verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='itemweaponranged',
            name='category',
            field=app.models.SingleChoiceField(blank=True, choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], max_length=100, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='itemweaponranged',
            name='tags',
            field=app.models.MultiChoiceField(blank=True, choices=[('General', (('ONE HANDED', 'One Handed'), ('TWO HANDED', 'Two Handed'), ('BASHING', 'Bashing'), ('CONCEALABLE', 'Concealable'), ('LETHAL', 'Lethal'), ('MOUNTED', 'Mounted'), ('PIERCING', 'Piercing'), ('SPECIAL', 'Special'))), ('Melee', (('MELEE', 'Melee'), ('BALANCED', 'Balanced'), ('BRAWL', 'Brawl'), ('CHOPPING', 'Chopping'), ('DISARMING', 'Disarming'), ('FLEXIBLE', 'Flexible'), ('IMPROVISED', 'Improvised'), ('GRAPPLING', 'Grappling'), ('MARTIAL ARTS', 'Martial Arts'), ('NATURAL', 'Natural'), ('REACHING', 'Reaching'), ('SHIELD', 'Shield'), ('SMASHING', 'Smashing'), ('WORN', 'Worn'))), ('Thrown', (('THROWN', 'Occult'), ('CUTTING', 'Cutting'), ('POISONABLE', 'Poisonable'), ('SUBTLE', 'Subtle'))), ('Archery', (('ARCHERY', 'Archery'), ('CROSSBOW', 'Crossbow'), ('FLAME', 'Flame'), ('POWERFUL', 'Powerful'), ('SLOW', 'Slow')))], max_length=100, verbose_name='Tags'),
        ),
    ]
