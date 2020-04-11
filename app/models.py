from django.db import models
import multiselectfield
from random import randint
from math import ceil

#==============================================================================#
#-------------------------------- OPTION LISTS --------------------------------#
#==============================================================================#
ATTRIBUTES = [
    (
        "Physical", (
            ("STR", "Srength"),
            ("DEX", "Dexterity"),
            ("STA", "Stamina"),
        ),
    ),
    (
        "Social", (
            ("CHA", "Charisma"),
            ("MAN", "Manipulation"),
            ("APP", "Appearance"),
        ),
    ),
    (
        "Mental", (
            ("PER", "Perception"),
            ("INT", "Intelligence"),
            ("WIT", "Wits"),
        ),
    ),
]

ABILITIES = [
    (
        "War", (
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
        "Life", (
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
        "Wisdom", (
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

TAGS_WEAPONS = [
    (
        "General", (
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
        "Melee", (
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
        "Thrown", (
            ("THROWN", "Occult"),
            ("CUTTING", "Cutting"),
            ("POISONABLE", "Poisonable"),
            ("SUBTLE", "Subtle"),
        ),
    ),
    (
        "Archery", (
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

DIE_TYPES = [
    ("NONE", "None"),
    ("SUCCESS", "Success"),
    ("DOUBLE", "Double"),
    ("EXPLODING_DISAPPEARING", "Exploding / Disappearing"),
    ("SUBTRACTING", "Subtracting")
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

class MultiChoiceField(multiselectfield.MultiSelectField):
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

class DieField(multiselectfield.MultiSelectField):
    def __init__(self, verbose_name, number, default, *args, **kwargs):
        self.number = number
        kwargs['verbose_name'] = verbose_name
        kwargs['default'] = default
        kwargs['choices'] = DIE_TYPES
        kwargs['blank'] = False
        kwargs['max_length'] = 100
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['number'] = self.number
        return name, path, args, kwargs

class NamedBooleanField(models.BooleanField):
    def __init__(self, verbose_name, default=False, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['default'] = default
        kwargs['blank'] = False
        super().__init__(*args, **kwargs)

class NamedForeignKeyField(models.ForeignKey):
    def __init__(self, verbose_name, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['on_delete'] = models.CASCADE
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)

class NamedManyToManyField(models.ManyToManyField):
    def __init__(self, verbose_name, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['blank'] = True
        super().__init__(*args, **kwargs)

class NamedOneToOneField(models.OneToOneField):
    def __init__(self, verbose_name, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['on_delete'] = models.CASCADE
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)

#==============================================================================#
#-------------------------------- DICE ROLLING --------------------------------#
#==============================================================================#
class rollConfiguration(models.Model):
    r01 = DieField("1s", 1, ["NONE"])
    r02 = DieField("2s", 2, ["NONE"])
    r03 = DieField("3s", 3, ["NONE"])
    r04 = DieField("4s", 4, ["NONE"])
    r05 = DieField("5s", 5, ["NONE"])
    r06 = DieField("6s", 6, ["NONE"])
    r07 = DieField("7s", 7, ["SUCCESS"])
    r08 = DieField("8s", 8, ["SUCCESS"])
    r09 = DieField("9s", 9, ["SUCCESS"])
    r10 = DieField("10s", 10, ["SUCCESS", "DOUBLE"])

    def roll(self, pool=1):
        listDice = [
            self.r01,
            self.r02,
            self.r03,
            self.r04,
            self.r05,
            self.r06,
            self.r07,
            self.r08,
            self.r09,
            self.r10,
        ]
        listSuccess, listDouble, listExplodingDisappearing, listSubtracting = [], [], [], []
        for die in listDice:
            if "SUCCESS" in die:
                listSuccess.append(die.number)
            if "DOUBLE" in die:
                listDouble.append(die.number)
            if "EXPLODING_DISAPPEARING" in die:
                listExplodingDisappearing.append(die.number)
            if "SUBTRACTING" in die:
                listSubtracting.append(die.number)
        successes = 0
        listExploded, listDisappeared = [], []
        listRoll = [0 for die in range(pool)]
        while 0 in listRoll:
            for die in listRoll:
                if die == 0:
                    die = randint(1, 10)
                if die in listExplodingDisappearing:
                    if die in listSuccess:
                        listExploded.append(die)
                    else:
                        listDisappeared.append(die)
                    die = 0
        for die in listRoll + listExploded:
            if die in listSuccess:
                successes += 1
            if die in listDouble:
                successes += 1
            if die in listSubtracting:
                successes -= 1
        if successes < 0:
            successes = 0
        botch = (successes == 0) and (1 in listRoll)
        return successes, botch, listRoll, listExploded, listDisappeared

#==============================================================================#
#--------------------------------- MODIFIERS ----------------------------------#
#==============================================================================#
class modifierBase(models.Model):
    class Meta:
        abstract = True
    value = NamedIntegerField("Modifier Value")

class modifierAttribute(modifierBase):
    def __str__(self):
        return "{} [{}]".format(self.attribute, self.value)

    attribute = SingleChoiceField("Attribute", ATTRIBUTES)

class modifierAbility(modifierBase):
    def __str__(self):
        return "{} [{}]".format(self.ability, self.value)

    ability = SingleChoiceField("Ability", ABILITIES)

class modifierStatic(modifierBase):
    def __str__(self):
        return "{} [{}]".format(self.static, self.value)

    static = SingleChoiceField("Static", STATICS)

#==============================================================================#
#--------------------------------- CHARACTERS ---------------------------------#
#==============================================================================#
class characterBase(models.Model):
    def __str__(self):
        return self.name

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
    archery        = DotField("Archery")
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
    # Reverse relation
    # .merit_set.all()

    #=========== WILLPOWER ============#
    willpowerCap = 10
    willpowerMax = NamedIntegerField("Maximum Willpower")
    willpower = NamedIntegerField("Current Willpower")

    #=========== EXPERIENCE ===========#
    experienceTotal = NamedIntegerField("Total Experience")
    experience = NamedIntegerField("Current Experience")

    #============ WEAPONS =============#
    # Reverse relation
    # .itemWeaponMelee_set.all()
    # .itemWeaponRanged_set.all()

    #============= ARMOR ==============#
    # Reverse relation
    # .itemArmor_set.all()

    #============= ITEMS ==============#
    # Reverse relation
    # .item_set.all()

    #============= HEALTH =============#
    health0 = NamedIntegerField("'-0' Health Levels")
    health1 = NamedIntegerField("'-1' Health Levels")
    health2 = NamedIntegerField("'-2' Health Levels")
    healthIndex = NamedIntegerField("Health Track Index")
    def healthTrack(self):
        return ["Healthy"] + ["-0" for i in range(self.health0)] + ["-1" for i in range(self.health1)] + ["-1" for i in range(self.health1)] + ["-4", "i"]
    def healthLevel(self):
        return self.healthTrack()[self.healthIndex]

    #============ STATICS =============#
    def resolve(self, speciality=None, mod=0):
        if self.charmsActive():
            mod += sum([])
        if speciality:
            mod += specility.modifier
        return mod + ceil((self.wits + self.integrity) / 2)
    def guile(self, speciality=None, mod=0):
        if self.charmsActive():
            mod += sum([])
        if speciality:
            mod += specility.modifier
        return mod + ceil((self.manipulation + self.socialize) / 2)
    def soakNatural(self, mod=0):
        if self.charmsActive():
            mod += sum([])
        return mod + self.stamina
    def soakArmored(self, mod=0):
        if self.armorEquipped.all():
            mod += sum([])
        return mod
    def soakTotal(self, mod=0):
        return mod + self.soakNatural() + self.soakArmored()
    def hardness(self, mod=0):
        if self.armorEquipped.all():
            mod += sum([])
        if self.charmsActive():
            mod += sum([])
        return mod
    def joinBattle(self, mod=0):
        if self.charmsActive():
            mod += sum([])
        return mod + self.wits + self.awareness + 3
    def evasion(self, mod=0):
        if self.charmsActive():
            mod += sum([])
        return mod + ceil((self.dexterity + self.dodge) / 2) - sum([])
    def rush(self, mod=0):
        if self.charmsActive():
            mod += sum([])
        return mod + self.dexterity + self.athletics
    def disengage(self, mod=0):
        if self.charmsActive():
            mod += sum([])
        return mod + self.dexterity + self.dodge

class characterExaltBase(characterBase):
    class Meta:
        abstract = True

    #============ ESSENCE =============#

    #============= LIMIT ==============#

    #======= EXALTED EXPERIENCE =======#

    #============= CHARMS =============#

    pass

class characterExaltSolar(characterExaltBase):

    #============ SUPERNAL ============#

    pass

class characterExaltLunar(characterExaltBase):

    #========= SHAPESHIFTING ==========#

    pass

#==============================================================================#
#----------------------------------- ITEMS ------------------------------------#
#==============================================================================#
class itemBase(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()
    character = NamedForeignKeyField("Character", characterBase)

class item(itemBase):
    pass

#==============================================================================#
#---------------------------------- WEAPONS -----------------------------------#
#==============================================================================#
class itemWeaponBase(itemBase):
    class Meta:
        abstract = True

    equipped = NamedBooleanField("Equipped?")
    category = SingleChoiceField("Category", CATEGORIES)
    tags = MultiChoiceField("Tags", TAGS_WEAPONS)
    accuracy = NamedIntegerField("Accuracy")
    damage = NamedIntegerField("Damage")
    defense = NamedIntegerField("Defense")
    overwhelming = NamedIntegerField("Overwhelming")
    attunement = NamedIntegerField("Attunement")

class itemWeaponMelee(itemWeaponBase):
    def attack(self, ability, mod=0, withering=True):
        if withering:
            return mod + ability + self.dexterity + weapon.accuracy
        else:
            return mod + ability + self.dexterity
    def parry(self, ability, mod=0):
        if self.character.charmsActive():
            mod += sum([])
        return mod + ceil((self.dexterity + ability) / 2) + weapon.defense

class itemWeaponRanged(itemWeaponBase):
    rangeClose = NamedIntegerField("Close Range")
    rangeShort = NamedIntegerField("Short Range")
    rangeMedium = NamedIntegerField("Medium Range")
    rangeLong = NamedIntegerField("Long Range")
    rangeExtreme = NamedIntegerField("Extreme Range")
    def attack(self, ability, rangeBand, mod=0, withering=True):
        rangeBand = rangeBand.lower()
        if rangeBand == "close" or rangeBand == "c":
            rangeModifier = self.rangeClose
        elif rangeBand == "short" or rangeBand == "s":
            rangeModifier = self.rangeShort
        elif rangeBand == "medium" or rangeBand == "m":
            rangeModifier = self.rangeMedium
        elif rangeBand == "long" or rangeBand == "l":
            rangeModifier = self.rangeLong
        elif rangeBand == "extreme" or rangeBand == "e":
            rangeModifier = self.rangeExtreme
        else:
            rangeModifier = 0
        if withering:
            return mod + rangeModifier + ability + self.dexterity + weapon.accuracy
        else:
            return mod + rangeModifier + ability + self.dexterity

#==============================================================================#
#----------------------------------- ARMOR ------------------------------------#
#==============================================================================#
class itemArmor(itemBase):
    equipped = NamedBooleanField("Equipped?")
    category = SingleChoiceField("Category", CATEGORIES)
    tags = MultiChoiceField("Tags", TAGS_ARMOR)
    soak = NamedIntegerField("Soak")
    hardness = NamedIntegerField("Hardness")
    mobilityPenalty = NamedIntegerField("Mobility Penalty")
    attunement = NamedIntegerField("Attunement")

#==============================================================================#
#----------------------------------- CHARMS -----------------------------------#
#==============================================================================#
class charmBase(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()
    levelEssence = NamedIntegerField("Essence Level")
    levelKey = NamedIntegerField("Key Level")
    character = NamedForeignKeyField("Character", characterBase)
    active = NamedBooleanField("Active?")
    rollConfiguration = NamedManyToManyField("Roll Configurations", rollConfiguration)
    modifierAttribute = NamedManyToManyField("Attribute Modifiers", modifierAttribute)
    modifierAbility = NamedManyToManyField("Abilities Modifiers", modifierAbility)
    modifierStatic = NamedManyToManyField("Statics Modifiers", modifierStatic)
    def modifier(self, keyword):
        output = 0
        for modifierAttribute in self.modifierAttribute.all():
            if keyword == modifierAttribute.attribute:
                output += modifierAttribute.value
        for modifierAbility in self.modifierAbility.all():
            if keyword == modifierAbility.ability:
                output += modifierAbility.value
        for modifierStatic in self.modifierStatic.all():
            if keyword == modifierStatic.static:
                output += modifierStatic.value
        return

class charmSolar(charmBase):
    ability = SingleChoiceField("Key Ability", ABILITIES)

class charmLunar(charmBase):
    attribute = SingleChoiceField("Key Attribute", ATTRIBUTES)

#==============================================================================#
#----------------------------------- MERITS -----------------------------------#
#==============================================================================#
class merit(models.Model):
    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()
    dots = DotField("Dots")
    character = NamedForeignKeyField("Character", characterBase)
    rollConfiguration = NamedManyToManyField("Roll Configurations", rollConfiguration)
    modifierAttribute = NamedManyToManyField("Attribute Modifiers", modifierAttribute)
    modifierAbility = NamedManyToManyField("Abilities Modifiers", modifierAbility)
    modifierStatic = NamedManyToManyField("Statics Modifiers", modifierStatic)

#==============================================================================#
#-------------------------------- SPECIALITIES --------------------------------#
#==============================================================================#
class speciality(models.Model):
    def __str__(self):
        return "[{}] {}".format(self.ability, self.name)

    modifier = 2
    name = NameField()
    ability = SingleChoiceField("Ability", ABILITIES)
    character = NamedForeignKeyField("Character", characterBase)

#==============================================================================#
#--------------------------------- INTIMACIES ---------------------------------#
#==============================================================================#
class intimacyBase(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return "[{}] {}".format(self.description, self.intensity)

    description = DescriptionField()
    intensity = SingleChoiceField("Intensity", INTENSITIES)
    character = NamedForeignKeyField("Character", characterBase)

class intimacyTie(intimacyBase):
    target = NamedCharField("Target")

class intimacyPrincipal(intimacyBase):
    pass

