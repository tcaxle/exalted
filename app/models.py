from django.db import models
from polymorphic.models import PolymorphicModel
import multiselectfield
from random import randint
from math import ceil

#==============================================================================#
#-------------------------------- OPTION LISTS --------------------------------#
#==============================================================================#
ATTRIBUTES = [
    (
        "Physical", (
            ("Strength", "Strength"),
            ("Dexterity", "Dexterity"),
            ("Stamina", "Stamina"),
        ),
    ),
    (
        "Social", (
            ("Charisma", "Charisma"),
            ("Manipulation", "Manipulation"),
            ("Appearance", "Appearance"),
        ),
    ),
    (
        "Mental", (
            ("Perception", "Perception"),
            ("Intelligence", "Intelligence"),
            ("Wits", "Wits"),
        ),
    ),
]

ABILITIES = [
    (
        "War", (
            ("Archery", "Archery"),
            ("Athletics", "Athletics"),
            ("Awareness", "Awareness"),
            ("Brawl", "Brawl"),
            ("Dodge", "Dodge"),
            ("Integrity", "Integrity"),
            ("Melee", "Melee"),
            ("Resistance", "Resistance"),
            ("Thrown", "Thrown"),
            ("War", "War"),
        ),
    ),
    (
        "Life", (
            ("Craft", "Craft"),
            ("Larceny", "Larceny"),
            ("Linguistics", "Linguistics"),
            ("Performance", "Performance"),
            ("Presence", "Presence"),
            ("Ride", "Ride"),
            ("Sail", "Sail"),
            ("Socialise", "Socialise"),
            ("Stealth", "Stealth"),
            ("Survival", "Survival"),
        ),
    ),
    (
        "Wisdom", (
            ("Bureaucracy", "Bureaucracy"),
            ("Investigation", "Investigation"),
            ("Lore", "Lore"),
            ("Medicine", "Medicine"),
            ("Occult", "Occult"),
        ),
    ),
]

ATTRIBUTE_TYPES = [
    ("Physical", "Physical"),
    ("Social", "Social"),
    ("Mental", "Mental"),
]

ABILITY_TYPES = [
    ("War", "War"),
    ("Life", "Life"),
    ("Wisdom", "Wisdom"),
    ("Additional", "Additional")
]

STATICS = [
    ("Natural Soak", "Natural Soak"),
    ("Armored Soak", "Armored Soak"),
    ("Total Soak", "Total Soak"),
    ("Hardness", "Hardness"),
    ("Parry", "Parry"),
    ("Evasion", "Evasion"),
    ("Resolve", "Resolve"),
    ("Guile", "Guile"),
    ("Rush", "Rush"),
    ("Disengage", "Disengage"),
    ("Join Battle", "Join Battle"),
]

CATEGORIES = [
    ("Light", "Light"),
    ("Medium", "Medium"),
    ("Heavy", "Heavy"),
]

TAGS_WEAPONS = [
    (
        "General", (
            ("One Handed", "One Handed"),
            ("Two Handed", "Two Handed"),
            ("Bashing", "Bashing"),
            ("Concealable", "Concealable"),
            ("Lethal", "Lethal"),
            ("Mounted", "Mounted"),
            ("Piercing", "Piercing"),
            ("Special", "Special"),
        ),
    ),
    (
        "Melee", (
            ("Melee", "Melee"),
            ("Balanced", "Balanced"),
            ("Brawl", "Brawl"),
            ("Chopping", "Chopping"),
            ("Disarming", "Disarming"),
            ("Flexible", "Flexible"),
            ("Improvised", "Improvised"),
            ("Grappling", "Grappling"),
            ("Martial Arts", "Martial Arts"),
            ("Natural", "Natural"),
            ("Reaching", "Reaching"),
            ("Shield", "Shield"),
            ("Smashing", "Smashing"),
            ("Worn", "Worn"),
        ),
    ),
    (
        "Thrown", (
            ("Thrown", "Thrown"),
            ("Occult", "Occult"),
            ("Cutting", "Cutting"),
            ("Poisonable", "Poisonable"),
            ("Subtle", "Subtle"),
        ),
    ),
    (
        "Archery", (
            ("Archery", "Archery"),
            ("Crossbow", "Crossbow"),
            ("Flame", "Flame"),
            ("Powerful", "Powerful"),
            ("Slow", "Slow"),
        ),
    ),
]

TAGS_ARMOR = [
    ("Buoyant", "Buoyant"),
    ("Concealable", "Concealable"),
    ("Silent", "Silent"),
]

INTENSITIES = [
    ("Minor", "Minor"),
    ("Major", "Major"),
    ("Defining", "Defining"),
]

DIE_TYPES = [
    ("None", "None"),
    ("Success", "Success"),
    ("Double", "Double"),
    ("Exploding / Disappearing", "Exploding / Disappearing"),
    ("Subtracting", "Subtracting")
]

CHARM_TYPES = [
    ("Permanent", "Permanent"),
    ("Simple", "Simple"),
    ("Reflexive", "Reflexive"),
    ("Suplemental", "Suplemental"),
]

CHARM_DURATIONS = [
    ("", ""),
    ("One Round", "One Round"),
    ("One Scene", "One Scene"),
    ("Indefinite", "Indefinite"),
]

CHARM_KEYWORDS = [
    (
        "Charms", (
            ("Advantage", "Advantage"),
            ("Attack-Action", "Attack-Action"),
            ("Counterattack", "Counterattack"),
            ("Form", "Form"),
            ("Group", "Group"),
            ("Mute", "Mute"),
            ("Perilous", "Perilous"),
            ("Once Per Scene", "Once Per Scene"),
            ("Once Per Day", "Once Per Day"),
            ("Once Per Story", "Once Per Story"),
            ("Once Per Season", "Once Per Season"),
            ("Pilot", "Pilot"),
            ("Post-Roll", "Post-Roll"),
            ("Psyche", "Psyche"),
            ("Quickshot", "Quickshot"),
        )
    ),
    (
        "Evocations", (
            ("Dissonant", "Dissonant"),
            ("Resonant", "Resonant"),
        )
    ),
]

CASTES_SOLAR = [
    ("Dawn", "Dawn"),
    ("Zenith", "Zenith"),
    ("Twilight", "Twilight"),
    ("Night", "Night"),
    ("Eclipse", "Eclipse"),
]

CASTES_LUNAR = [
    ("Full Moon", "Full Moon"),
    ("Changing Moon", "Changing Moon"),
    ("No Moon", "No Moon"),
    ("Castless", "Castless")
]

SHAPE_SIZES = [
    ("Normal", "Normal"),
]

SHAPE_TYPES = [
    ("Human", "Human"),
    ("Animal", "Animal"),
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
class RollConfiguration(PolymorphicModel):
    def __str__(self):
        return self.name
    name = NameField()
    successesAuto = NamedIntegerField("Auto-Successes")
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

    def roll(self, pool=1, successesStunt=0):
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
        successes = self.successesAuto + successesStunt
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
#--------------------------------- PROPERTIES ---------------------------------#
#==============================================================================#
class PropertyBase(PolymorphicModel):
    name = NameField()
    description = DescriptionField()

class PropertyAttribute(PropertyBase):
    propertyType = SingleChoiceField("Type", ATTRIBUTE_TYPES)
    core = NamedBooleanField("Core?")

class PropertyAbility(PropertyBase):
    propertyType = SingleChoiceField("Type", ABILITY_TYPES)

class PropertyStatic(PropertyBase):
    propertyType = None

#==============================================================================#
#--------------------------------- MODIFIERS ----------------------------------#
#==============================================================================#
class ModifierBase(PolymorphicModel):
    value = NamedIntegerField("Modifier Value")

class ModifierAttribute(ModifierBase):
    def __str__(self):
        return "{} [{}]".format(self.keyword, self.value)

    keyword = SingleChoiceField("Attribute", ATTRIBUTES)

class ModifierAbility(ModifierBase):
    def __str__(self):
        return "{} [{}]".format(self.keyword, self.value)

    keyword = SingleChoiceField("Ability", ABILITIES)

class ModifierStatic(ModifierBase):
    def __str__(self):
        return "{} [{}]".format(self.keyword, self.value)

    keyword = SingleChoiceField("Static", STATICS)

#==============================================================================#
#--------------------------------- CHARACTERS ---------------------------------#
#==============================================================================#
class CharacterBase(PolymorphicModel):
    def __str__(self):
        return self.name

    #======== MODIFIER METHODS ========#
    def effectModifier(self, PropertyBase):
        modifier = 0
        try:
            ownerships = [ownership for ownership in ownershipBase.objects.all() if (ownership.owner == self) and (ownership.active)]
            for ownership in ownerships:
                try:
                    modifier += ownership.target.modifier(keyword)
                except:
                    pass
        except:
            pass
        return modifier

    #============ GENERAL =============#
    name = NameField()
    player = models.CharField(verbose_name="Player", max_length=100, blank=True)
    concept = models.TextField(blank=True)

    #=========== ATTRIBUTES ===========#
    # Reverse Reference
    def attributeSet(self):
        try:
            return [ownership.target for ownership in self.OwnershipPropertyAttribute_set.all()]
        except:
            return None

    #=========== ABILITIES ============#
    # Reverse Reference
    def abilitySet(self):
        output = []
        try:
            ownerships = self.ownershipPropertyAbility_set.order_by("target__name")
            output.append(("War", [ownership for ownership in ownerships if ownership.target.propertyType=="War"]))
            output.append(("Life", [ownership for ownership in ownerships if ownership.target.propertyType=="Life"]))
            output.append(("Wisdom", [ownership for ownership in ownerships if ownership.target.propertyType=="Wisdom"]))
            output.append(("Additional", [ownership for ownership in ownerships if ownership.target.propertyType=="Additional"]))
        except:
            output.append(("War", []))
            output.append(("Life", []))
            output.append(("Wisdom", []))
            output.append(("Additional", []))
        return output

    #============= MERITS =============#
    # Reverse relation
    def meritSet(self):
        output = []
        try:
            ownerships = self.ownershipMerit_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #========== SPECIALITIES ==========#
    # Reverse relation
    def specialitySet(self):
        output = []
        try:
            ownerships = self.ownershipSpeciality_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #=========== INTIMACIES ===========#
    # Reverse relation
    # character.intimactBase_set.all()
    # character.intimacyTie_set.object.all()
    # character.intimacyPrincipal_set.all()

    #=========== WILLPOWER ============#
    willpowerMax = NamedIntegerField("Maximum Willpower")
    willpower = NamedIntegerField("Current Willpower")
    def dotsTriWillpower(self):
        output = [0 for i in range(10)]
        for i in range(10):
            if i < self.willpowerMax and i >= self.willpower:
                output[i] = 1
            elif i < self.willpower:
                output[i] = 2
        return output


    #=========== EXPERIENCE ===========#
    experienceTotal = NamedIntegerField("Total Experience")
    experience = NamedIntegerField("Current Experience")

    #============ WEAPONS =============#
    # Reverse relation
    def itemWeaponSet(self):
        output = []
        try:
            ownerships = self.ownershipItemWeapon_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #============= ARMOR ==============#
    # Reverse relation
    def itemArmorSet(self):
        output = []
        try:
            ownerships = self.ownershipItemArmor_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output
    def armorSoak(self):
        armor = None
        modifier = 0
        try:
            armor = self.itemArmorSet().filter(equipped=True)
        except:
            pass
        if armor:
            for item in armor:
                modifier += item.soak
        return modifier
    def armorHardness(self):
        armor = None
        modifier = 0
        try:
            armor = self.itemArmorSet().filter(equipped=True)
        except:
            pass
        if armor:
            for item in armor:
                modifier += item.hardness
        return modifier
    def armorMobilityPenalty(self):
        armor = None
        modifier = 0
        try:
            armor = self.itemArmorSet().filter(equipped=True)
        except:
            pass
        if armor:
            for item in armor:
                modifier += item.mobilityPenalty
        return modifier

    #============= ITEMS ==============#
    # Reverse relation
    def itemSet(self):
        output = []
        try:
            ownerships = self.ownershipItem_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #============ ESSENCE =============#
    essence = NamedIntegerField("Essence")
    def dotsEssence(self):
        output = []
        for i in range(self.essence):
            output.append(True)
        for i in range(5 - self.essence):
            output.append(False)
        return output

    #============= HEALTH =============#
    health0 = NamedIntegerField("'-0' Health Levels")
    health1 = NamedIntegerField("'-1' Health Levels")
    health2 = NamedIntegerField("'-2' Health Levels")
    healthIndex = NamedIntegerField("Health Track Index")
    def healthTrack(self):
        return ["Healthy"] + ["-0" for i in range(self.health0)] + ["-1" for i in range(self.health1)] + ["-1" for i in range(self.health1)] + ["-4", "i"]
    def healthLevel(self):
        return self.healthTrack()[self.healthIndex]
    def healthDots(self):
        output = []
        for i in range(len(self.healthTrack()) - 1):
            output.append((self.healthTrack()[i+1], i < self.healthIndex))
        return output

    #============ STATICS =============#
#    def resolve(self, speciality=None, mod=0):
#        return mod + ceil((self.attributeWits() + self.abilityIntegrity()) / 2) + self.effectModifier("RESOLVE")
#
#    def guile(self, speciality=None, mod=0):
#        return mod + ceil((self.attributeManipulation() + self.abilitySocialize()) / 2) + self.effectModifier("GUILE")
#
#    def soakNatural(self, mod=0):
#        return mod + self.attributeStamina() + self.effectModifier("SOAK NATURAL")
#
#    def soakArmored(self, mod=0):
#        return mod + self.armorSoak()
#
#    def soakTotal(self, mod=0):
#        return mod + self.soakNatural() + self.soakArmored()
#
#    def hardness(self, mod=0):
#        return mod + self.armorHardness() + self.effectModifier("HARDNESS")
#
#    def joinBattle(self, mod=0):
#        return mod + self.attributeWits() + self.abilityAwareness() + 3 + self.effectModifier("JOIN BATTLE")
#
#    def evasion(self, mod=0):
#        return mod + ceil((self.attributeDexterity() + self.abilityDodge()) / 2) - self.armorMobilityPenalty() + self.effectModifier("EVASION")
#
#    def rush(self, mod=0):
#        return mod + self.attributeDexterity() + self.abilityAthletics() + self.effectModifier("RUSH")
#
#    def disengage(self, mod=0):
#        return mod + self.attributeDexterity() + self.abilityDodge() + self.effectModifier("DISENGAGE")

class CharacterMortal(CharacterBase):
    def type(self):
        return "Mortal"

class CharacterExaltBase(CharacterBase):
    anima = models.CharField(verbose_name="Anima", max_length=100)

    #============= MOTES ==============#
    motesPersonalMax = NamedIntegerField("Maximum Personal Motes")
    motesPersonal = NamedIntegerField("Current Personal Motes")
    motesPeripheralMax = NamedIntegerField("Maximum Peripheral Motes")
    motesPeripheral = NamedIntegerField("Current Peripheral Motes")
    motesCommitted = NamedIntegerField("Committed Motes")

    #============= LIMIT ==============#
    limitTrigger = models.TextField(verbose_name="Limit Trigger", blank="False", max_length=1000)
    limitBreak = NamedIntegerField("Limit Break")
    def dotsLimit(self):
        output = [False for i in range(10)]
        for i in range(10):
            output[i] = i < self.limitBreak
        return output

    #======= EXALTED EXPERIENCE =======#
    experienceExaltedTotal = NamedIntegerField("Total Exalted Experience")
    experienceExalted = NamedIntegerField("Current Exalted Experience")

    #========== MARTIAL ARTS ==========#
    # Reverse relation
    def martialArtSet(self):
        output = []
        try:
            ownerships = self.ownershipCharmMartialArt_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #=========== EVOCATIONS ===========#
    # Reverse relation
    def evocationSet(self):
        output = []
        try:
            ownerships = self.ownershipCharmEvocation_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

class CharacterExaltSolar(CharacterExaltBase):
    def type(self):
        return "Solar Exalt"

    caste = SingleChoiceField("Solar Caste", CASTES_SOLAR)
    #============= CHARMS =============#
    # Reverse relation
    def charmSet(self):
        output = []
        try:
            ownerships = self.ownershipCharmSolar_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #======= SUPERNAL & FAVORED =======#
    abilitySupernal = SingleChoiceField("Supernal Ability", ABILITIES)
    abilityFavored = MultiChoiceField("Favoured Abilities", ABILITIES)

class CharacterExaltLunar(CharacterExaltBase):
    def type(self):
        return "Lunar Exalt"

    caste = SingleChoiceField("Lunar Caste", CASTES_LUNAR)
    #========= SHAPESHIFTING ==========#
    spiritShape = models.CharField(verbose_name="Spirit Shape", max_length=100)
    # Reverse relation
    def lunarShapeSet(self):
        output = []
        try:
            ownerships = self.ownershipCharmLunarShape_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #============= CHARMS =============#
    # Reverse relation
    def charmSet(self):
        output = []
        try:
            ownerships = self.ownershipCharmLunar_set.all()
            for ownership in ownerships:
                output.append(ownership.target)
        except:
            pass
        return output

    #============ FAVORED =============#
    attributeFavored = MultiChoiceField("Favoured Attributes", ATTRIBUTES)

#==============================================================================#
#----------------------------------- ITEMS ------------------------------------#
#==============================================================================#
class ItemBase(PolymorphicModel):
    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()

class Item(ItemBase):
    pass

#==============================================================================#
#---------------------------------- WEAPONS -----------------------------------#
#==============================================================================#
class ItemWeaponBase(ItemBase):
    category = SingleChoiceField("Category", CATEGORIES)
    tags = MultiChoiceField("Tags", TAGS_WEAPONS)
    accuracy = NamedIntegerField("Accuracy")
    damage = NamedIntegerField("Damage")
    defense = NamedIntegerField("Defense")
    overwhelming = NamedIntegerField("Overwhelming")
    attunement = NamedIntegerField("Attunement")

class ItemWeaponMelee(ItemWeaponBase):
    def attack(self, ability, mod=0, withering=True):
        if withering:
            return mod + ability + self.dexterity + weapon.accuracy
        else:
            return mod + ability + self.dexterity
    def parry(self, ability, mod=0):
        if self.character.charmsActive():
            mod += sum([])
        return mod + ceil((self.dexterity + ability) / 2) + weapon.defense

class ItemWeaponRanged(ItemWeaponBase):
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
class ItemArmor(ItemBase):
    category = SingleChoiceField("Category", CATEGORIES)
    tags = MultiChoiceField("Tags", TAGS_ARMOR)
    soak = NamedIntegerField("Soak")
    hardness = NamedIntegerField("Hardness")
    mobilityPenalty = NamedIntegerField("Mobility Penalty")
    attunement = NamedIntegerField("Attunement")

#==============================================================================#
#---------------------------------- EFFECTS -----------------------------------#
#==============================================================================#

class EffectBase(PolymorphicModel):
    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()
    rollConfiguration = NamedManyToManyField("Roll Configurations", RollConfiguration)
    modifiers = NamedManyToManyField("Modifiers", ModifierBase)
    def modifier(self, keyword):
        output = 0
        for modifier in self.modifiers.all():
            if keyword == modifier.keyword:
                output += modifier.value
        return output

#==============================================================================#
#----------------------------------- CHARMS -----------------------------------#
#==============================================================================#
class CharmBase(EffectBase):
    levelEssence = NamedIntegerField("Essence Level")
    charmType = SingleChoiceField("Charm Type", CHARM_TYPES)
    duration = SingleChoiceField("Charm Duration", CHARM_DURATIONS)
    keywords = MultiChoiceField("Charm Keywords", CHARM_KEYWORDS)

class CharmMartialArt(CharmBase):
    def type(self):
        return "Martial Art"
    levelKey = NamedIntegerField("Martial Arts Level")
    key = None

class CharmEvocation(CharmBase):
    def type(self):
        return "Evocation"
    levelKey = 0
    key = NamedForeignKeyField("Artifact", ItemBase)

class CharmSolar(CharmBase):
    def type(self):
        return "Solar"
    levelKey = NamedIntegerField("Ability Level")
    key = SingleChoiceField("Key Ability", ABILITIES)

class CharmLunar(CharmBase):
    def type(self):
        return "Lunar"
    levelKey = NamedIntegerField("Attribute Level")
    key = SingleChoiceField("Key Attribute", ATTRIBUTES)

class CharmLunarShape(CharmBase):
    levelKey = 0
    def type(self):
        return "Lunar Shape"
    key = None
    size = SingleChoiceField("Size", SHAPE_SIZES)
    shapeType = SingleChoiceField("Shape Type", SHAPE_TYPES)

#==============================================================================#
#----------------------------------- MERITS -----------------------------------#
#==============================================================================#
class Merit(EffectBase):
    dots = DotField("Dots")
    def dotsDisplay(self):
        output = []
        for i in range(self.dots):
            output.append(True)
        for i in range(5 - self.dots):
            output.append(False)
        return output

#==============================================================================#
#-------------------------------- SPECIALITIES --------------------------------#
#==============================================================================#
class Speciality(EffectBase):
    pass
#==============================================================================#
#--------------------------------- INTIMACIES ---------------------------------#
#==============================================================================#
class IntimacyBase(PolymorphicModel):
    def __str__(self):
        return "[{}] {}".format(self.description, self.intensity)

    description = DescriptionField()
    intensity = SingleChoiceField("Intensity", INTENSITIES)
    character = NamedForeignKeyField("Character", CharacterBase, related_name="intimacy_set")

class IntimacyTie(IntimacyBase):
    target = NamedCharField("Target")

class IntimacyPrincipal(IntimacyBase):
    pass

#==============================================================================#
#--------------------------------- OWNERSHIP ----------------------------------#
#==============================================================================#
class OwnershipBase(PolymorphicModel):
    notes = models.TextField(verbose_name="Notes", blank=True)
    active = NamedBooleanField("Active/Equipped?")

class OwnershipItem(OwnershipBase):
    target = NamedForeignKeyField("Item", Item, related_name="ownershipItemTarget_set")
    owner = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipItem_set")
class OwnershipItemWeapon(OwnershipBase):
    target = NamedForeignKeyField("Weapon", ItemWeaponBase, related_name="ownershipItemWeaponTarget_set")
    owner = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipItemWeapon_set")
class OwnershipItemArmor(OwnershipBase):
    target = NamedForeignKeyField("Armor", ItemArmor, related_name="ownershipItemArmorTarget_set")
    owner = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipItemArmor_set")

class OwnershipPropertyAttribute(OwnershipBase):
    target = NamedForeignKeyField("Attribute", PropertyAttribute, related_name="ownershipPropertyAttributeTarget_set")
    character = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipPropertyAttribute_set")
    value = NamedIntegerField("Dots")
    def dots(self):
        output = []
        for i in range(self.value):
            output.append(True)
        for i in range(5 - self.value):
            output.append(False)
        return output
class OwnershipPropertyAbility(OwnershipBase):
    target = NamedForeignKeyField("Ability", PropertyAbility, related_name="ownershipPropertyAbilityTarget_set")
    character = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipPropertyAbility_set")
    value = NamedIntegerField("Dots")
    def dots(self):
        output = []
        for i in range(self.value):
            output.append(True)
        for i in range(5 - self.value):
            output.append(False)
        return output
class OwnershipPropertyStatic(OwnershipBase):
    target = NamedForeignKeyField("Static", PropertyStatic, related_name="ownershipPropertyStaticTarget_set")
    character = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipPropertyStaticTarget_set")

class OwnershipCharmMartialArt(OwnershipBase):
    target = NamedForeignKeyField("Martial Arts Charm", CharmMartialArt, related_name="ownershipCharmMartialArtTarget_set")
    owner = NamedForeignKeyField("Exalted Owner", CharacterExaltBase, related_name="ownershipCharmMartialArt_set")
class OwnershipCharmEvocation(OwnershipBase):
    target = NamedForeignKeyField("Evocation", CharmEvocation, related_name="ownershipCharmEvocationTarget_set")
    owner = NamedForeignKeyField("Exalted Owner", CharacterExaltBase, related_name="ownershipCharmEvocation_set")
class OwnershipCharmSolar(OwnershipBase):
    target = NamedForeignKeyField("Solar Charm", CharmSolar, related_name="ownershipCharmSolarTarget_set")
    owner = NamedForeignKeyField("Solar Exalted Owner", CharacterExaltSolar, related_name="ownershipCharmSolar_set")
class OwnershipCharmLunar(OwnershipBase):
    target = NamedForeignKeyField("Lunar Charm", CharmLunar, related_name="ownershipCharmLunarTarget_set")
    owner = NamedForeignKeyField("Lunar Exalted Owner", CharacterExaltLunar, related_name="ownershipCharmLunar_set")
class OwnershipCharmLunarShape(OwnershipBase):
    target = NamedForeignKeyField("Lunar Shape", CharmLunarShape, related_name="ownershipCharmLunarShapeTarget_set")
    owner = NamedForeignKeyField("Lunar Exalted Owner", CharacterExaltLunar, related_name="ownershipCharmLunarShape_set")

class OwnershipMerit(OwnershipBase):
    target = NamedForeignKeyField("Merit", Merit, related_name="ownershipMeritTarget_set")
    owner = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipMerit_set")

class OwnershipSpeciality(OwnershipBase):
    target = NamedForeignKeyField("Speciality", Speciality, related_name="ownershipSpecialityTarget_set")
    owner = NamedForeignKeyField("Owner", CharacterBase, related_name="ownershipSpeciality_set")
