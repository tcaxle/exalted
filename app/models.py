from django.db import models

#==============================================================================#
#-------------------------------- OPTION LISTS --------------------------------#
#==============================================================================#
ATTRIBUTES = [
    (
        "Physical" (
            ("STR", "Srength"),
            ("DEX", "Dexterity"),
            ("STA", "Stamina"),
        ),
    ),
    (
        "Social" (
            ("CHA", "Charisma"),
            ("MAN", "Manipulation"),
            ("APP", "Appearance"),
        ),
    ),
    (
        "Mental" (
            ("PER", "Perception"),
            ("INT", "Intelligence"),
            ("WIT", "Wits"),
        ),
    ),
]

ABILITIES = [
    (
        "War" (
            ("ARCHERY", "Archery"),
            ("ATHLETICS", "Athletics"),
            ("AWARENESS", "Awareness"),
            ("BRAWL", "Brawl"),
            ("DODGE", "Dodge"),
            ("INTEGRITY", "Integrity"),
            ("MELEE", "Melee"),
            ("RESISTANCE", "Resistance"),
            ("THROWN", "Thrown"),
            ("WAR", "War"),
        ),
    ),
    (
        "Life" (
            ("CRAFT", "Craft"),
            ("LARCENY", "Larceny"),
            ("LINGUISTICS", "Linguistics"),
            ("PERFORMANCE", "Performance"),
            ("PRESENCE", "Presence"),
            ("RIDE", "Ride"),
            ("SAIL", "Sail"),
            ("SOCIALISE", "Socialise"),
            ("STEALTH", "Stealth"),
            ("SURVIVAL", "Survival"),
        ),
    ),
    (
        "Wisdom" (
            ("BUREAUCRACY", "Bureaucracy"),
            ("INVESTIGATION", "Investigation"),
            ("LORE", "Lore"),
            ("MEDICINE", "Medicine"),
            ("OCCULT", "Occult"),
        ),
    ),
]

STATICS = [
    ("SOAK NATURAL", "Natural Soak"),
    ("SOAK ARMORED", "Armored Soak"),
    ("SOAK TOTAL", "Total Soak"),
    ("HARDNESS", "Hardness"),
    ("PARRY", "Parry"),
    ("EVASION", "Evasion"),
    ("RESOLVE", "Resolve"),
    ("GUILE", "Guile"),
    ("RUSH", "Rush"),
    ("DISENGAGE", "Disengage"),
    ("JOIN BATTLE", "Join Battle"),
]

CATEGORIES = [
    ("L", "Light"),
    ("M", "Medium"),
    ("H", "Heavy"),
]

TAGS_WEAPON = [
    (
        "General" (
            ("ONE HANDED", "One Handed"),
            ("TWO HANDED", "Two Handed"),
            ("BASHING", "Bashing"),
            ("CONCEALABLE", "Concealable"),
            ("LETHAL", "Lethal"),
            ("MOUNTED", "Mounted"),
            ("PIERCING", "Piercing"),
            ("SPECIAL", "Special"),
        ),
    ),
    (
        "Melee" (
            ("MELEE", "Melee"),
            ("BALANCED", "Balanced"),
            ("BRAWL", "Brawl"),
            ("CHOPPING", "Chopping"),
            ("DISARMING", "Disarming"),
            ("FLEXIBLE", "Flexible"),
            ("IMPROVISED", "Improvised"),
            ("GRAPPLING", "Grappling"),
            ("MARTIAL ARTS", "Martial Arts"),
            ("NATURAL", "Natural"),
            ("REACHING", "Reaching"),
            ("SHIELD", "Shield"),
            ("SMASHING", "Smashing"),
            ("WORN", "Worn"),
        ),
    ),
    (
        "Thrown" (
            ("THROWN", "Occult"),
            ("CUTTING", "Cutting"),
            ("POISONABLE", "Poisonable"),
            ("SUBTLE", "Subtle"),
        ),
    ),
    (
        "Archery" (
            ("ARCHERY", "Archery"),
            ("CROSSBOW", "Crossbow"),
            ("FLAME", "Flame"),
            ("POWERFUL", "Powerful"),
            ("SLOW", "Slow"),
        ),
    ),
]

TAGS_ARMOR = [
    ("BUOYANT", "Buoyant"),
    ("CONCEALABLE", "Concealable"),
    ("SILENT", "Silent"),
]

INTENSITIES = [
    ("MINOR", "Minor"),
    ("MAJOR", "Major"),
    ("DEFINING", "Defining"),
]

#==============================================================================#
#------------------------------- CUSTOM MODELS --------------------------------#
#==============================================================================#
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = "Name"
        kwargs['blank'] = False
        kwargs['max_length'] = 100
        super().__init__(*args, **kwargs)

class DescriptionField(models.TextField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = "Description"
        kwargs['blank'] = True
        kwargs['max_length'] = 1000
        super().__init__(*args, **kwargs)

class DotField(models.IntegerField):
    def __init__(self, verbose_name, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['blank'] = False
        kwargs['default'] = 0
        super().__init__(*args, **kwargs)

class SingleChoiceField(models.CharField):
    def __init__(self, verbose_name, choices, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['choices'] = choices
        kwargs['blank'] = True
        kwargs['max_length'] = 100
        super().__init__(*args, **kwargs)

class NamedIntegerField(models.IntegerField):
    def __init__(self, verbose_name, desc=None, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['help_text'] = desc
        kwargs['blank'] = False
        kwargs['default'] = 0
        super().__init__(*args, **kwargs)

class NamedCharField(models.CharField):
    def __init__(self, verbose_name, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['blank'] = False
        kwargs['max_length'] = 100
        super().__init__(*args, **kwargs)

#==============================================================================#
#--------------------------------- MODIFIERS ----------------------------------#
#==============================================================================#
class modifierBase(models.Model):
    class Meta:
        abstract = True
    value = NamedIntegerField("Modifier Value")

class modifierAttribute(modifierBase):
    attribute = SingleChoiceField("Attribute", ATTRIBUTES)

class modifierAbility(modifierBase):
    ability = SingleChoiceField("Ability", ABIILITIES)

class modifierStatic(modifierBase):
    static = SingleChoiceField("Static", STATICS)

#==============================================================================#
#----------------------------------- ITEMS ------------------------------------#
#==============================================================================#
class itemBase(models.Model):
    class Meta:
        abstract = True

    name = NameField()
    description = DescriptionField()

class item(itemBase):
    pass

#==============================================================================#
#---------------------------------- WEAPONS -----------------------------------#
#==============================================================================#
class itemWeaponBase(itemBase):
    class Meta:
        abstract = True

    # category
    # tags
    accuracy = NamedIntegerField("Accuracy")
    damage = NamedIntegerField("Damage")
    defense = NamedIntegerField("Defense")
    overwhelming = NamedIntegerField("Overwhelming")
    attunement = NamedIntegerField("Attunement")

class itemWeaponMelee(itemWeaponBase):
    pass

class itemWeaponRanged(itemWeaponBase):
    rangeClose = NamedIntegerField("Close Range")
    rangeShort = NamedIntegerField("Short Range")
    rangeMedium = NamedIntegerField("Medium Range")
    rangeLong = NamedIntegerField("Long Range")
    rangeExtreme = NamedIntegerField("Extreme Range")

#==============================================================================#
#----------------------------------- ARMOR ------------------------------------#
#==============================================================================#
class itemArmor(itemBase):
    # category
    # tags
    soak = NamedIntegerField("Soak")
    hardness = NamedIntegerField("Hardness")
    mobilityPenalty = NamedIntegerField("Mobility Penalty")
    attunement = NamedIntegerField("Attunement")

#==============================================================================#
#----------------------------------- CHARMS -----------------------------------#
#==============================================================================#
class charm(models.Model):
    name = NameField()
    description = DescriptionField()
    # modifierAttribute
    # modifierAbility
    # modifierStatic
    # rollConfiguration

#==============================================================================#
#----------------------------------- MERITS -----------------------------------#
#==============================================================================#
class merit(models.Model):
    name = NameField()
    description = DescriptionField()
    dots = DotField("Dots")
    # modifierAttribute
    # modifierAbility
    # modifierStatic
    # rollConfiguration

#==============================================================================#
#-------------------------------- SPECIALITIES --------------------------------#
#==============================================================================#
class speciality(models.Model):
    modifier = 2
    name = NameField()
    # ability

#==============================================================================#
#--------------------------------- INTIMACIES ---------------------------------#
#==============================================================================#
class intimacyBase(models.Model):
    class Meta:
        abstract = True

    description = DescriptionField()
    intensity = SingleChoiceField("Intensity", INTENSITIES)
    pass

class intimacyTie(intimacyBase):
    target = NamedCharField("Target")
    pass

class intimacyPrincipal(intimacyBase):
    pass

#==============================================================================#
#--------------------------------- CHARACTERS ---------------------------------#
#==============================================================================#
class characterBase(models.Model):
    class Meta:
        abstract = True

    #============ GENERAL =============#
    name = NameField()

    #=========== ATTRIBUTES ===========#
    strength      = DotField("Strength")
    dexterity     = DotField("Dexterity")
    stamina       = DotField("Stamina")
    charisma      = DotField("Charisma")
    manipulation  = DotField("Manipulation")
    appearance    = DotField("Apperance")
    perception    = DotField("Perception")
    intelligence  = DotField("Intelligence")
    wits          = DotField("Wits")

    #=========== ABILITIES ============#
    archey        = DotField("Archery")
    athletics     = DotField("Athletics")
    awareness     = DotField("Awareness")
    brawl         = DotField("Brawl")
    bureaucracy   = DotField("Bureaucracy")
    craft         = DotField("Craft")
    dodge         = DotField("Dodge")
    integrity     = DotField("Integrity")
    investigation = DotField("Investigation")
    larceny       = DotField("Larceny")
    linguistics   = DotField("Linguistics")
    lore          = DotField("Lore")
    martialArts   = DotField("MartialArts")
    medicine      = DotField("Medicine")
    melee         = DotField("Melee")
    occult        = DotField("Occult")
    performance   = DotField("Performance")
    presence      = DotField("Presence")
    resistance    = DotField("Resistance")
    ride          = DotField("Ride")
    sail          = DotField("Sail")
    socialize     = DotField("Socialize")
    stealth       = DotField("Stealth")
    survival      = DotField("Survival")
    thrown        = DotField("Thrown")
    war           = DotField("War")

    #============= MERITS =============#

    #=========== WILLPOWER ============#

    #=========== EXPERIENCE ===========#

    #============ WEAPONS =============#

    #============= ARMOR ==============#

    #============= ITEMS ==============#

    #============= HEALTH =============#

    #============ STATICS =============#

class characterExaltBase(characterBase):
    class Meta:
        abstract = True

    #============ ESSENCE =============#

    #============= LIMIT ==============#

    #======= EXALTED EXPERIENCE =======#

    #============= CHARMS =============#

    pass

class characterMortal(characterBase):
    pass

class characterExaltSolar(characterExaltBase):

    #============ SUPERNAL ============#

    pass

class characterExaltLunar(characterExaltBase):

    #========= SHAPESHIFTING ==========#

    pass
