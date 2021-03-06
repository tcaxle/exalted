# Generated by Django 3.0.5 on 2020-04-17 21:26

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0003_auto_20200416_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', app.models.NameField(max_length=100, verbose_name='Name')),
                ('description', app.models.DescriptionField(blank=True, max_length=1000, verbose_name='Description')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_app.propertybase_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
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
            model_name='characterexaltbase',
            name='characterbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharacterBase'),
        ),
        migrations.AlterField(
            model_name='characterexaltlunar',
            name='characterexaltbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharacterExaltBase'),
        ),
        migrations.AlterField(
            model_name='characterexaltsolar',
            name='characterexaltbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharacterExaltBase'),
        ),
        migrations.AlterField(
            model_name='charactermortal',
            name='characterbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharacterBase'),
        ),
        migrations.AlterField(
            model_name='charmbase',
            name='effectbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.EffectBase'),
        ),
        migrations.AlterField(
            model_name='charmevocation',
            name='charmbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharmBase'),
        ),
        migrations.AlterField(
            model_name='charmevocation',
            name='key',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ItemBase', verbose_name='Artifact'),
        ),
        migrations.AlterField(
            model_name='charmlunar',
            name='charmbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharmBase'),
        ),
        migrations.AlterField(
            model_name='charmlunarshape',
            name='charmbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharmBase'),
        ),
        migrations.AlterField(
            model_name='charmmartialart',
            name='charmbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharmBase'),
        ),
        migrations.AlterField(
            model_name='charmsolar',
            name='charmbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.CharmBase'),
        ),
        migrations.AlterField(
            model_name='effectbase',
            name='modifiers',
            field=app.models.NamedManyToManyField(blank=True, to='app.ModifierBase', verbose_name='Modifiers'),
        ),
        migrations.AlterField(
            model_name='effectbase',
            name='rollConfiguration',
            field=app.models.NamedManyToManyField(blank=True, to='app.RollConfiguration', verbose_name='Roll Configurations'),
        ),
        migrations.AlterField(
            model_name='intimacybase',
            name='character',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intimacy_set', to='app.CharacterBase', verbose_name='Character'),
        ),
        migrations.AlterField(
            model_name='intimacyprincipal',
            name='intimacybase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.IntimacyBase'),
        ),
        migrations.AlterField(
            model_name='intimacytie',
            name='intimacybase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.IntimacyBase'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itembase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ItemBase'),
        ),
        migrations.AlterField(
            model_name='itemarmor',
            name='itembase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ItemBase'),
        ),
        migrations.AlterField(
            model_name='itemweaponbase',
            name='itembase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ItemBase'),
        ),
        migrations.AlterField(
            model_name='itemweaponmelee',
            name='itemweaponbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ItemWeaponBase'),
        ),
        migrations.AlterField(
            model_name='itemweaponranged',
            name='itemweaponbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ItemWeaponBase'),
        ),
        migrations.AlterField(
            model_name='merit',
            name='effectbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.EffectBase'),
        ),
        migrations.AlterField(
            model_name='modifierability',
            name='modifierbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ModifierBase'),
        ),
        migrations.AlterField(
            model_name='modifierattribute',
            name='modifierbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ModifierBase'),
        ),
        migrations.AlterField(
            model_name='modifierstatic',
            name='modifierbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.ModifierBase'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmevocation',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmEvocation_set', to='app.CharacterExaltBase', verbose_name='Exalted Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmevocation',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmevocation',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmEvocationTarget_set', to='app.CharmEvocation', verbose_name='Evocation'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmlunar',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmLunar_set', to='app.CharacterExaltLunar', verbose_name='Lunar Exalted Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmlunar',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmlunar',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmLunarTarget_set', to='app.CharmLunar', verbose_name='Lunar Charm'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmlunarshape',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmLunarShape_set', to='app.CharacterExaltLunar', verbose_name='Lunar Exalted Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmlunarshape',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmlunarshape',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmLunarShapeTarget_set', to='app.CharmLunarShape', verbose_name='Lunar Shape'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmmartialart',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmMartialArt_set', to='app.CharacterExaltBase', verbose_name='Exalted Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmmartialart',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmmartialart',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmMartialArtTarget_set', to='app.CharmMartialArt', verbose_name='Martial Arts Charm'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmsolar',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmSolar_set', to='app.CharacterExaltSolar', verbose_name='Solar Exalted Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmsolar',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipcharmsolar',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipCharmSolarTarget_set', to='app.CharmSolar', verbose_name='Solar Charm'),
        ),
        migrations.AlterField(
            model_name='ownershipitem',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipItem_set', to='app.CharacterBase', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipitem',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipitem',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipItemTarget_set', to='app.Item', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='ownershipitemarmor',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipItemArmor_set', to='app.CharacterBase', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipitemarmor',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipitemarmor',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipItemArmorTarget_set', to='app.ItemArmor', verbose_name='Armor'),
        ),
        migrations.AlterField(
            model_name='ownershipitemweapon',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipItemWeapon_set', to='app.CharacterBase', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipitemweapon',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipitemweapon',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipItemWeaponTarget_set', to='app.ItemWeaponBase', verbose_name='Weapon'),
        ),
        migrations.AlterField(
            model_name='ownershipmerit',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipMerit_set', to='app.CharacterBase', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipmerit',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipmerit',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipMeritTarget_set', to='app.Merit', verbose_name='Merit'),
        ),
        migrations.AlterField(
            model_name='ownershipspeciality',
            name='owner',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipSpeciality_set', to='app.CharacterBase', verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='ownershipspeciality',
            name='ownershipbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase'),
        ),
        migrations.AlterField(
            model_name='ownershipspeciality',
            name='target',
            field=app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipSpecialityTarget_set', to='app.Speciality', verbose_name='Speciality'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='effectbase_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.EffectBase'),
        ),
        migrations.CreateModel(
            name='PropertyAbility',
            fields=[
                ('propertybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.PropertyBase')),
                ('propertyType', app.models.SingleChoiceField(blank=True, choices=[('War', 'War'), ('Life', 'Life'), ('Wisdom', 'Wisdom'), ('Additional', 'Additional')], max_length=100, verbose_name='Type')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.propertybase',),
        ),
        migrations.CreateModel(
            name='PropertyAttribute',
            fields=[
                ('propertybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.PropertyBase')),
                ('propertyType', app.models.SingleChoiceField(blank=True, choices=[('Physical', 'Physical'), ('Social', 'Social'), ('Mental', 'Mental')], max_length=100, verbose_name='Type')),
                ('core', app.models.NamedBooleanField(default=False, verbose_name='Core?')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.propertybase',),
        ),
        migrations.CreateModel(
            name='PropertyStatic',
            fields=[
                ('propertybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.PropertyBase')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.propertybase',),
        ),
        migrations.CreateModel(
            name='OwnershipStatic',
            fields=[
                ('ownershipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase')),
                ('character', app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CharacterBase', verbose_name='Owner')),
                ('target', app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PropertyStatic', verbose_name='Static')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.ownershipbase',),
        ),
        migrations.CreateModel(
            name='OwnershipPropertyAttribute',
            fields=[
                ('ownershipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase')),
                ('value', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Dots')),
                ('character', app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipPropertyAttribute_set', to='app.CharacterBase', verbose_name='Owner')),
                ('target', app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownershipPropertyAttributeTarget_set', to='app.PropertyAttribute', verbose_name='Attribute')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.ownershipbase',),
        ),
        migrations.CreateModel(
            name='OwnershipPropertyAbility',
            fields=[
                ('ownershipbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.OwnershipBase')),
                ('value', app.models.NamedIntegerField(default=0, help_text=None, verbose_name='Dots')),
                ('character', app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.CharacterBase', verbose_name='Owner')),
                ('target', app.models.NamedForeignKeyField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PropertyAbility', verbose_name='Ability')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('app.ownershipbase',),
        ),
    ]
