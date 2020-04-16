from django.contrib import admin
from .models import *

admin.site.register(RollConfiguration)

admin.site.register(ModifierAttribute)
admin.site.register(ModifierAbility)
admin.site.register(ModifierStatic)

admin.site.register(Item)
admin.site.register(ItemWeaponMelee)
admin.site.register(ItemWeaponRanged)
admin.site.register(ItemArmor)

admin.site.register(CharmSolar)
admin.site.register(CharmLunar)
admin.site.register(CharmLunarShape)
admin.site.register(CharmEvocation)
admin.site.register(CharmMartialArt)

admin.site.register(Merit)

admin.site.register(Speciality)

admin.site.register(IntimacyTie)
admin.site.register(IntimacyPrincipal)

admin.site.register(CharacterMortal)
admin.site.register(CharacterExaltSolar)
admin.site.register(CharacterExaltLunar)

admin.site.register(OwnershipItem)
admin.site.register(OwnershipItemWeapon)
admin.site.register(OwnershipItemArmor)
admin.site.register(OwnershipCharmMartialArt)
admin.site.register(OwnershipCharmEvocation)
admin.site.register(OwnershipCharmSolar)
admin.site.register(OwnershipCharmLunar)
admin.site.register(OwnershipCharmLunarShape)
admin.site.register(OwnershipMerit)
admin.site.register(OwnershipSpeciality)
