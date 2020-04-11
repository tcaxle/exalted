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

admin.site.register(merit)

admin.site.register(speciality)

admin.site.register(intimacyTie)
admin.site.register(intimacyPrincipal)

admin.site.register(characterBase)
admin.site.register(characterExaltSolar)
admin.site.register(characterExaltLunar)
