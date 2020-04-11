# Generated by Django 3.0.5 on 2020-04-11 14:59

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='intimacyPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('intensity', app.models.SingleChoiceField(blank=True, choices=[('MINOR', 'Minor'), ('MAJOR', 'Major'), ('DEFINING', 'Defining')], max_length=100, verbose_name='Intensity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='intimacyTie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('intensity', app.models.SingleChoiceField(blank=True, choices=[('MINOR', 'Minor'), ('MAJOR', 'Major'), ('DEFINING', 'Defining')], max_length=100, verbose_name='Intensity')),
                ('target', app.models.NamedCharField(max_length=100, verbose_name='Target')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='itemArmor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('category', app.models.SingleChoiceField(blank=True, choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], max_length=100, verbose_name='Category')),
                ('tags', app.models.MultiChoiceField(blank=True, choices=[('BUOYANT', 'Buoyant'), ('CONCEALABLE', 'Concealable'), ('SILENT', 'Silent')], max_length=100, verbose_name='Tags')),
                ('soak', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Soak')),
                ('hardness', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Hardness')),
                ('mobilityPenalty', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Mobility Penalty')),
                ('attunement', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Attunement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='itemWeaponMelee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('category', app.models.SingleChoiceField(blank=True, choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], max_length=100, verbose_name='Category')),
                ('tags', app.models.MultiChoiceField(blank=True, choices=[('General', (('ONE HANDED', 'One Handed'), ('TWO HANDED', 'Two Handed'), ('BASHING', 'Bashing'), ('CONCEALABLE', 'Concealable'), ('LETHAL', 'Lethal'), ('MOUNTED', 'Mounted'), ('PIERCING', 'Piercing'), ('SPECIAL', 'Special'))), ('Melee', (('MELEE', 'Melee'), ('BALANCED', 'Balanced'), ('BRAWL', 'Brawl'), ('CHOPPING', 'Chopping'), ('DISARMING', 'Disarming'), ('FLEXIBLE', 'Flexible'), ('IMPROVISED', 'Improvised'), ('GRAPPLING', 'Grappling'), ('MARTIAL ARTS', 'Martial Arts'), ('NATURAL', 'Natural'), ('REACHING', 'Reaching'), ('SHIELD', 'Shield'), ('SMASHING', 'Smashing'), ('WORN', 'Worn'))), ('Thrown', (('THROWN', 'Occult'), ('CUTTING', 'Cutting'), ('POISONABLE', 'Poisonable'), ('SUBTLE', 'Subtle'))), ('Archery', (('ARCHERY', 'Archery'), ('CROSSBOW', 'Crossbow'), ('FLAME', 'Flame'), ('POWERFUL', 'Powerful'), ('SLOW', 'Slow')))], max_length=100, verbose_name='Tags')),
                ('accuracy', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Accuracy')),
                ('damage', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Damage')),
                ('defense', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Defense')),
                ('overwhelming', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Overwhelming')),
                ('attunement', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Attunement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='itemWeaponRanged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('category', app.models.SingleChoiceField(blank=True, choices=[('L', 'Light'), ('M', 'Medium'), ('H', 'Heavy')], max_length=100, verbose_name='Category')),
                ('tags', app.models.MultiChoiceField(blank=True, choices=[('General', (('ONE HANDED', 'One Handed'), ('TWO HANDED', 'Two Handed'), ('BASHING', 'Bashing'), ('CONCEALABLE', 'Concealable'), ('LETHAL', 'Lethal'), ('MOUNTED', 'Mounted'), ('PIERCING', 'Piercing'), ('SPECIAL', 'Special'))), ('Melee', (('MELEE', 'Melee'), ('BALANCED', 'Balanced'), ('BRAWL', 'Brawl'), ('CHOPPING', 'Chopping'), ('DISARMING', 'Disarming'), ('FLEXIBLE', 'Flexible'), ('IMPROVISED', 'Improvised'), ('GRAPPLING', 'Grappling'), ('MARTIAL ARTS', 'Martial Arts'), ('NATURAL', 'Natural'), ('REACHING', 'Reaching'), ('SHIELD', 'Shield'), ('SMASHING', 'Smashing'), ('WORN', 'Worn'))), ('Thrown', (('THROWN', 'Occult'), ('CUTTING', 'Cutting'), ('POISONABLE', 'Poisonable'), ('SUBTLE', 'Subtle'))), ('Archery', (('ARCHERY', 'Archery'), ('CROSSBOW', 'Crossbow'), ('FLAME', 'Flame'), ('POWERFUL', 'Powerful'), ('SLOW', 'Slow')))], max_length=100, verbose_name='Tags')),
                ('accuracy', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Accuracy')),
                ('damage', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Damage')),
                ('defense', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Defense')),
                ('overwhelming', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Overwhelming')),
                ('attunement', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Attunement')),
                ('rangeClose', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Close Range')),
                ('rangeShort', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Short Range')),
                ('rangeMedium', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Medium Range')),
                ('rangeLong', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Long Range')),
                ('rangeExtreme', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Extreme Range')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='modifierAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Modifier Value')),
                ('ability', app.models.SingleChoiceField(blank=True, choices=[('War', (('ARCHERY', 'Archery'), ('ATHLETICS', 'Athletics'), ('AWARENESS', 'Awareness'), ('BRAWL', 'Brawl'), ('DODGE', 'Dodge'), ('INTEGRITY', 'Integrity'), ('MELEE', 'Melee'), ('RESISTANCE', 'Resistance'), ('THROWN', 'Thrown'), ('WAR', 'War'))), ('Life', (('CRAFT', 'Craft'), ('LARCENY', 'Larceny'), ('LINGUISTICS', 'Linguistics'), ('PERFORMANCE', 'Performance'), ('PRESENCE', 'Presence'), ('RIDE', 'Ride'), ('SAIL', 'Sail'), ('SOCIALISE', 'Socialise'), ('STEALTH', 'Stealth'), ('SURVIVAL', 'Survival'))), ('Wisdom', (('BUREAUCRACY', 'Bureaucracy'), ('INVESTIGATION', 'Investigation'), ('LORE', 'Lore'), ('MEDICINE', 'Medicine'), ('OCCULT', 'Occult')))], max_length=100, verbose_name='Ability')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='modifierAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Modifier Value')),
                ('attribute', app.models.SingleChoiceField(blank=True, choices=[('Physical', (('STR', 'Srength'), ('DEX', 'Dexterity'), ('STA', 'Stamina'))), ('Social', (('CHA', 'Charisma'), ('MAN', 'Manipulation'), ('APP', 'Appearance'))), ('Mental', (('PER', 'Perception'), ('INT', 'Intelligence'), ('WIT', 'Wits')))], max_length=100, verbose_name='Attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='modifierStatic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Modifier Value')),
                ('static', app.models.SingleChoiceField(blank=True, choices=[('SOAK NATURAL', 'Natural Soak'), ('SOAK ARMORED', 'Armored Soak'), ('SOAK TOTAL', 'Total Soak'), ('HARDNESS', 'Hardness'), ('PARRY', 'Parry'), ('EVASION', 'Evasion'), ('RESOLVE', 'Resolve'), ('GUILE', 'Guile'), ('RUSH', 'Rush'), ('DISENGAGE', 'Disengage'), ('JOIN BATTLE', 'Join Battle')], max_length=100, verbose_name='Static')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='rollConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r01', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['NONE'], max_length=100, number=1, verbose_name='1s')),
                ('r02', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['NONE'], max_length=100, number=2, verbose_name='2s')),
                ('r03', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['NONE'], max_length=100, number=3, verbose_name='3s')),
                ('r04', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['NONE'], max_length=100, number=4, verbose_name='4s')),
                ('r05', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['NONE'], max_length=100, number=5, verbose_name='5s')),
                ('r06', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['NONE'], max_length=100, number=6, verbose_name='6s')),
                ('r07', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['SUCCESS'], max_length=100, number=7, verbose_name='7s')),
                ('r08', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['SUCCESS'], max_length=100, number=8, verbose_name='8s')),
                ('r09', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['SUCCESS'], max_length=100, number=9, verbose_name='9s')),
                ('r10', app.models.DieField(choices=[('NONE', 'None'), ('SUCCESS', 'Success'), ('DOUBLE', 'Double'), ('EXPLODING_DISAPPEARING', 'Exploding / Disappearing'), ('SUBTRACTING', 'Subtracting')], default=['SUCCESS', 'DOUBLE'], max_length=100, number=10, verbose_name='10s')),
            ],
        ),
        migrations.CreateModel(
            name='speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('ability', app.models.SingleChoiceField(blank=True, choices=[('War', (('ARCHERY', 'Archery'), ('ATHLETICS', 'Athletics'), ('AWARENESS', 'Awareness'), ('BRAWL', 'Brawl'), ('DODGE', 'Dodge'), ('INTEGRITY', 'Integrity'), ('MELEE', 'Melee'), ('RESISTANCE', 'Resistance'), ('THROWN', 'Thrown'), ('WAR', 'War'))), ('Life', (('CRAFT', 'Craft'), ('LARCENY', 'Larceny'), ('LINGUISTICS', 'Linguistics'), ('PERFORMANCE', 'Performance'), ('PRESENCE', 'Presence'), ('RIDE', 'Ride'), ('SAIL', 'Sail'), ('SOCIALISE', 'Socialise'), ('STEALTH', 'Stealth'), ('SURVIVAL', 'Survival'))), ('Wisdom', (('BUREAUCRACY', 'Bureaucracy'), ('INVESTIGATION', 'Investigation'), ('LORE', 'Lore'), ('MEDICINE', 'Medicine'), ('OCCULT', 'Occult')))], max_length=100, verbose_name='Ability')),
            ],
        ),
        migrations.CreateModel(
            name='merit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('dots', app.models.DotField(default=0, verbose_name='Dots')),
                ('modifierAbility', app.models.NamedManyToManyField(blank=True, to='app.modifierAbility', verbose_name='Abilities Modifiers')),
                ('modifierAttribute', app.models.NamedManyToManyField(blank=True, to='app.modifierAttribute', verbose_name='Attribute Modifiers')),
                ('modifierStatic', app.models.NamedManyToManyField(blank=True, to='app.modifierStatic', verbose_name='Statics Modifiers')),
                ('rollConfiguration', app.models.NamedManyToManyField(blank=True, to='app.rollConfiguration', verbose_name='Roll Configurations')),
            ],
        ),
        migrations.CreateModel(
            name='charm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('modifierAbility', app.models.NamedManyToManyField(blank=True, to='app.modifierAbility', verbose_name='Abilities Modifiers')),
                ('modifierAttribute', app.models.NamedManyToManyField(blank=True, to='app.modifierAttribute', verbose_name='Attribute Modifiers')),
                ('modifierStatic', app.models.NamedManyToManyField(blank=True, to='app.modifierStatic', verbose_name='Statics Modifiers')),
                ('rollConfiguration', app.models.NamedManyToManyField(blank=True, to='app.rollConfiguration', verbose_name='Roll Configurations')),
            ],
        ),
        migrations.CreateModel(
            name='characterMortal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('strength', app.models.DotField(default=0, verbose_name='Strength')),
                ('dexterity', app.models.DotField(default=0, verbose_name='Dexterity')),
                ('stamina', app.models.DotField(default=0, verbose_name='Stamina')),
                ('charisma', app.models.DotField(default=0, verbose_name='Charisma')),
                ('manipulation', app.models.DotField(default=0, verbose_name='Manipulation')),
                ('appearance', app.models.DotField(default=0, verbose_name='Apperance')),
                ('perception', app.models.DotField(default=0, verbose_name='Perception')),
                ('intelligence', app.models.DotField(default=0, verbose_name='Intelligence')),
                ('wits', app.models.DotField(default=0, verbose_name='Wits')),
                ('archey', app.models.DotField(default=0, verbose_name='Archery')),
                ('athletics', app.models.DotField(default=0, verbose_name='Athletics')),
                ('awareness', app.models.DotField(default=0, verbose_name='Awareness')),
                ('brawl', app.models.DotField(default=0, verbose_name='Brawl')),
                ('bureaucracy', app.models.DotField(default=0, verbose_name='Bureaucracy')),
                ('craft', app.models.DotField(default=0, verbose_name='Craft')),
                ('dodge', app.models.DotField(default=0, verbose_name='Dodge')),
                ('integrity', app.models.DotField(default=0, verbose_name='Integrity')),
                ('investigation', app.models.DotField(default=0, verbose_name='Investigation')),
                ('larceny', app.models.DotField(default=0, verbose_name='Larceny')),
                ('linguistics', app.models.DotField(default=0, verbose_name='Linguistics')),
                ('lore', app.models.DotField(default=0, verbose_name='Lore')),
                ('martialArts', app.models.DotField(default=0, verbose_name='MartialArts')),
                ('medicine', app.models.DotField(default=0, verbose_name='Medicine')),
                ('melee', app.models.DotField(default=0, verbose_name='Melee')),
                ('occult', app.models.DotField(default=0, verbose_name='Occult')),
                ('performance', app.models.DotField(default=0, verbose_name='Performance')),
                ('presence', app.models.DotField(default=0, verbose_name='Presence')),
                ('resistance', app.models.DotField(default=0, verbose_name='Resistance')),
                ('ride', app.models.DotField(default=0, verbose_name='Ride')),
                ('sail', app.models.DotField(default=0, verbose_name='Sail')),
                ('socialize', app.models.DotField(default=0, verbose_name='Socialize')),
                ('stealth', app.models.DotField(default=0, verbose_name='Stealth')),
                ('survival', app.models.DotField(default=0, verbose_name='Survival')),
                ('thrown', app.models.DotField(default=0, verbose_name='Thrown')),
                ('war', app.models.DotField(default=0, verbose_name='War')),
                ('willpowerMax', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Maximum Willpower')),
                ('willpower', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Current Willpower')),
                ('experienceTotal', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Total Experience')),
                ('experience', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Current Experience')),
                ('health0', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-0' Health Levels")),
                ('health1', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-1' Health Levels")),
                ('health2', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-2' Health Levels")),
                ('healthIndex', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Health Track Index')),
                ('armor', app.models.NamedManyToManyField(blank=True, to='app.itemArmor', verbose_name='Armor')),
                ('items', app.models.NamedManyToManyField(blank=True, to='app.item', verbose_name='Items')),
                ('merits', app.models.NamedManyToManyField(blank=True, to='app.merit', verbose_name='Merits')),
                ('weaponsMelee', app.models.NamedManyToManyField(blank=True, to='app.itemWeaponMelee', verbose_name='Melee Weapons')),
                ('weaponsRanged', app.models.NamedManyToManyField(blank=True, to='app.itemWeaponRanged', verbose_name='Ranged Weapons')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='characterExaltSolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('strength', app.models.DotField(default=0, verbose_name='Strength')),
                ('dexterity', app.models.DotField(default=0, verbose_name='Dexterity')),
                ('stamina', app.models.DotField(default=0, verbose_name='Stamina')),
                ('charisma', app.models.DotField(default=0, verbose_name='Charisma')),
                ('manipulation', app.models.DotField(default=0, verbose_name='Manipulation')),
                ('appearance', app.models.DotField(default=0, verbose_name='Apperance')),
                ('perception', app.models.DotField(default=0, verbose_name='Perception')),
                ('intelligence', app.models.DotField(default=0, verbose_name='Intelligence')),
                ('wits', app.models.DotField(default=0, verbose_name='Wits')),
                ('archey', app.models.DotField(default=0, verbose_name='Archery')),
                ('athletics', app.models.DotField(default=0, verbose_name='Athletics')),
                ('awareness', app.models.DotField(default=0, verbose_name='Awareness')),
                ('brawl', app.models.DotField(default=0, verbose_name='Brawl')),
                ('bureaucracy', app.models.DotField(default=0, verbose_name='Bureaucracy')),
                ('craft', app.models.DotField(default=0, verbose_name='Craft')),
                ('dodge', app.models.DotField(default=0, verbose_name='Dodge')),
                ('integrity', app.models.DotField(default=0, verbose_name='Integrity')),
                ('investigation', app.models.DotField(default=0, verbose_name='Investigation')),
                ('larceny', app.models.DotField(default=0, verbose_name='Larceny')),
                ('linguistics', app.models.DotField(default=0, verbose_name='Linguistics')),
                ('lore', app.models.DotField(default=0, verbose_name='Lore')),
                ('martialArts', app.models.DotField(default=0, verbose_name='MartialArts')),
                ('medicine', app.models.DotField(default=0, verbose_name='Medicine')),
                ('melee', app.models.DotField(default=0, verbose_name='Melee')),
                ('occult', app.models.DotField(default=0, verbose_name='Occult')),
                ('performance', app.models.DotField(default=0, verbose_name='Performance')),
                ('presence', app.models.DotField(default=0, verbose_name='Presence')),
                ('resistance', app.models.DotField(default=0, verbose_name='Resistance')),
                ('ride', app.models.DotField(default=0, verbose_name='Ride')),
                ('sail', app.models.DotField(default=0, verbose_name='Sail')),
                ('socialize', app.models.DotField(default=0, verbose_name='Socialize')),
                ('stealth', app.models.DotField(default=0, verbose_name='Stealth')),
                ('survival', app.models.DotField(default=0, verbose_name='Survival')),
                ('thrown', app.models.DotField(default=0, verbose_name='Thrown')),
                ('war', app.models.DotField(default=0, verbose_name='War')),
                ('willpowerMax', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Maximum Willpower')),
                ('willpower', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Current Willpower')),
                ('experienceTotal', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Total Experience')),
                ('experience', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Current Experience')),
                ('health0', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-0' Health Levels")),
                ('health1', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-1' Health Levels")),
                ('health2', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-2' Health Levels")),
                ('healthIndex', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Health Track Index')),
                ('armor', app.models.NamedManyToManyField(blank=True, to='app.itemArmor', verbose_name='Armor')),
                ('items', app.models.NamedManyToManyField(blank=True, to='app.item', verbose_name='Items')),
                ('merits', app.models.NamedManyToManyField(blank=True, to='app.merit', verbose_name='Merits')),
                ('weaponsMelee', app.models.NamedManyToManyField(blank=True, to='app.itemWeaponMelee', verbose_name='Melee Weapons')),
                ('weaponsRanged', app.models.NamedManyToManyField(blank=True, to='app.itemWeaponRanged', verbose_name='Ranged Weapons')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='characterExaltLunar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('strength', app.models.DotField(default=0, verbose_name='Strength')),
                ('dexterity', app.models.DotField(default=0, verbose_name='Dexterity')),
                ('stamina', app.models.DotField(default=0, verbose_name='Stamina')),
                ('charisma', app.models.DotField(default=0, verbose_name='Charisma')),
                ('manipulation', app.models.DotField(default=0, verbose_name='Manipulation')),
                ('appearance', app.models.DotField(default=0, verbose_name='Apperance')),
                ('perception', app.models.DotField(default=0, verbose_name='Perception')),
                ('intelligence', app.models.DotField(default=0, verbose_name='Intelligence')),
                ('wits', app.models.DotField(default=0, verbose_name='Wits')),
                ('archey', app.models.DotField(default=0, verbose_name='Archery')),
                ('athletics', app.models.DotField(default=0, verbose_name='Athletics')),
                ('awareness', app.models.DotField(default=0, verbose_name='Awareness')),
                ('brawl', app.models.DotField(default=0, verbose_name='Brawl')),
                ('bureaucracy', app.models.DotField(default=0, verbose_name='Bureaucracy')),
                ('craft', app.models.DotField(default=0, verbose_name='Craft')),
                ('dodge', app.models.DotField(default=0, verbose_name='Dodge')),
                ('integrity', app.models.DotField(default=0, verbose_name='Integrity')),
                ('investigation', app.models.DotField(default=0, verbose_name='Investigation')),
                ('larceny', app.models.DotField(default=0, verbose_name='Larceny')),
                ('linguistics', app.models.DotField(default=0, verbose_name='Linguistics')),
                ('lore', app.models.DotField(default=0, verbose_name='Lore')),
                ('martialArts', app.models.DotField(default=0, verbose_name='MartialArts')),
                ('medicine', app.models.DotField(default=0, verbose_name='Medicine')),
                ('melee', app.models.DotField(default=0, verbose_name='Melee')),
                ('occult', app.models.DotField(default=0, verbose_name='Occult')),
                ('performance', app.models.DotField(default=0, verbose_name='Performance')),
                ('presence', app.models.DotField(default=0, verbose_name='Presence')),
                ('resistance', app.models.DotField(default=0, verbose_name='Resistance')),
                ('ride', app.models.DotField(default=0, verbose_name='Ride')),
                ('sail', app.models.DotField(default=0, verbose_name='Sail')),
                ('socialize', app.models.DotField(default=0, verbose_name='Socialize')),
                ('stealth', app.models.DotField(default=0, verbose_name='Stealth')),
                ('survival', app.models.DotField(default=0, verbose_name='Survival')),
                ('thrown', app.models.DotField(default=0, verbose_name='Thrown')),
                ('war', app.models.DotField(default=0, verbose_name='War')),
                ('willpowerMax', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Maximum Willpower')),
                ('willpower', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Current Willpower')),
                ('experienceTotal', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Total Experience')),
                ('experience', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Current Experience')),
                ('health0', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-0' Health Levels")),
                ('health1', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-1' Health Levels")),
                ('health2', app.models.NamedIntegerField(default=0, help_text=None, verbose_name="'-2' Health Levels")),
                ('healthIndex', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Health Track Index')),
                ('armor', app.models.NamedManyToManyField(blank=True, to='app.itemArmor', verbose_name='Armor')),
                ('items', app.models.NamedManyToManyField(blank=True, to='app.item', verbose_name='Items')),
                ('merits', app.models.NamedManyToManyField(blank=True, to='app.merit', verbose_name='Merits')),
                ('weaponsMelee', app.models.NamedManyToManyField(blank=True, to='app.itemWeaponMelee', verbose_name='Melee Weapons')),
                ('weaponsRanged', app.models.NamedManyToManyField(blank=True, to='app.itemWeaponRanged', verbose_name='Ranged Weapons')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
