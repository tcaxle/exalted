from django.contrib import admin
from .models import *

admin.site.register(rollConfiguration)

admin.site.register(modifierAttribute)
admin.site.register(modifierAbility)
admin.site.register(modifierStatic)

admin.site.register(item)
admin.site.register(itemWeaponMelee)
admin.site.register(itemWeaponRanged)
admin.site.register(itemArmor)

admin.site.register(charmSolar)
admin.site.register(charmLunar)
admin.site.register(charmLunarShape)
admin.site.register(charmEvocation)

admin.site.register(merit)

admin.site.register(speciality)

admin.site.register(intimacyTie)
admin.site.register(intimacyPrincipal)

admin.site.register(characterMortal)
admin.site.register(characterExaltSolar)
admin.site.register(characterExaltLunar)

admin.site.register(ownershipItem)
admin.site.register(ownershipItemWeapon)
admin.site.register(ownershipItemArmor)
admin.site.register(ownershipCharmMartialArt)
admin.site.register(ownershipCharmEvocation)
admin.site.register(ownershipCharmSolar)
admin.site.register(ownershipCharmLunar)
admin.site.register(ownershipCharmLunarShape)
admin.site.register(ownershipMerit)
admin.site.register(ownershipSpeciality)
