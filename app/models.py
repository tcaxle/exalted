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
class rollConfiguration(PolymorphicModel):
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
#--------------------------------- MODIFIERS ----------------------------------#
#==============================================================================#
class modifierBase(PolymorphicModel):
    value = NamedIntegerField("Modifier Value")

class modifierAttribute(modifierBase):
    def __str__(self):
        return "{} [{}]".format(self.keyword, self.value)

    keyword = SingleChoiceField("Attribute", ATTRIBUTES)

class modifierAbility(modifierBase):
    def __str__(self):
        return "{} [{}]".format(self.keyword, self.value)

    keyword = SingleChoiceField("Ability", ABILITIES)

class modifierStatic(modifierBase):
    def __str__(self):
        return "{} [{}]".format(self.keyword, self.value)

    keyword = SingleChoiceField("Static", STATICS)

#==============================================================================#
#--------------------------------- CHARACTERS ---------------------------------#
#==============================================================================#
class characterBase(PolymorphicModel):
    def __str__(self):
        return self.name

    #======== MODIFIER METHODS ========#
    def effectModifier(self, keyword):
        modifier = 0
        try:
            ownerships = self.ownershipBase_set.filter(active=True)
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
    strength = DotField("Strength")
    def attributeStrength(self):
        return self.strength + self.effectModifier("STRENGTH")
    def dotsStrength(self):
        output = []
        for i in range(self.strength):
            output.append(True)
        for i in range(5 - self.strength):
            output.append(False)
        return output
    dexterity = DotField("Dexterity")
    def attributeDexterity(self):
        return self.dexterity + self.effectModifier("DEXTERITY")
    def dotsDexterity(self):
        output = []
        for i in range(self.dexterity):
            output.append(True)
        for i in range(5 - self.dexterity):
            output.append(False)
        return output
    stamina = DotField("Stamina")
    def attributeStamina(self):
        return self.stamina + self.effectModifier("STAMINA")
    def dotsStamina(self):
        output = []
        for i in range(self.stamina):
            output.append(True)
        for i in range(5 - self.stamina):
            output.append(False)
        return output
    charisma = DotField("Charisma")
    def attributeCharisma(self):
        return self.charisma + self.effectModifier("CHARISMA")
    def dotsCharisma(self):
        output = []
        for i in range(self.charisma):
            output.append(True)
        for i in range(5 - self.charisma):
            output.append(False)
        return output
    manipulation = DotField("Manipulation")
    def attributeManipulation(self):
        return self.manipulation + self.effectModifier("MANIPULATION")
    def dotsManipulation(self):
        output = []
        for i in range(self.manipulation):
            output.append(True)
        for i in range(5 - self.manipulation):
            output.append(False)
        return output
    appearance = DotField("Apperance")
    def attributeAppearance(self):
        return self.appearance + self.effectModifier("APPEARANCE")
    def dotsAppearance(self):
        output = []
        for i in range(self.appearance):
            output.append(True)
        for i in range(5 - self.appearance):
            output.append(False)
        return output
    perception = DotField("Perception")
    def attributePerception(self):
        return self.perception + self.effectModifier("PERCEPTION")
    def dotsPerception(self):
        output = []
        for i in range(self.perception):
            output.append(True)
        for i in range(5 - self.perception):
            output.append(False)
        return output
    intelligence = DotField("Intelligence")
    def attributeIntelligence(self):
        return self.intelligence + self.effectModifier("INTELLIGENCE")
    def dotsIntelligence(self):
        output = []
        for i in range(self.intelligence):
            output.append(True)
        for i in range(5 - self.intelligence):
            output.append(False)
        return output
    wits = DotField("Wits")
    def attributeWits(self):
        return self.wits + self.effectModifier("WITS")
    def dotsWits(self):
        output = []
        for i in range(self.wits):
            output.append(True)
        for i in range(5 - self.wits):
            output.append(False)
        return output

    #=========== ABILITIES ============#
    archery = DotField("Archery")
    def abilityArchery(self):
        return self.archery + self.effectModifier("ARCHERY")
    def dotsArchery(self):
        output = []
        for i in range(self.archery):
            output.append(True)
        for i in range(5 - self.archery):
            output.append(False)
        return output
    athletics = DotField("Athletics")
    def abilityAthletics(self):
        return self.athletics + self.effectModifier("ATHLETICS")
    def dotsAthletics(self):
        output = []
        for i in range(self.athletics):
            output.append(True)
        for i in range(5 - self.athletics):
            output.append(False)
        return output
    awareness = DotField("Awareness")
    def abilityAwareness(self):
        return self.awareness + self.effectModifier("AWARENESS")
    def dotsAwareness(self):
        output = []
        for i in range(self.awareness):
            output.append(True)
        for i in range(5 - self.awareness):
            output.append(False)
        return output
    brawl = DotField("Brawl")
    def abilityBrawl(self):
        return self.brawl + self.effectModifier("BRAWL")
    def dotsBrawl(self):
        output = []
        for i in range(self.brawl):
            output.append(True)
        for i in range(5 - self.brawl):
            output.append(False)
        return output
    bureaucracy = DotField("Bureaucracy")
    def abilityBureaucracy(self):
        return self.bureaucracy + self.effectModifier("BUREAUCRACY")
    def dotsBureaucracy(self):
        output = []
        for i in range(self.bureaucracy):
            output.append(True)
        for i in range(5 - self.bureaucracy):
            output.append(False)
        return output
    craft = DotField("Craft")
    def abilityCraft(self):
        return self.craft + self.effectModifier("CRAFT")
    def dotsCraft(self):
        output = []
        for i in range(self.craft):
            output.append(True)
        for i in range(5 - self.craft):
            output.append(False)
        return output
    dodge = DotField("Dodge")
    def abilityDodge(self):
        return self.dodge + self.effectModifier("DODGE")
    def dotsDodge(self):
        output = []
        for i in range(self.dodge):
            output.append(True)
        for i in range(5 - self.dodge):
            output.append(False)
        return output
    integrity = DotField("Integrity")
    def abilityIntegrity(self):
        return self.integrity + self.effectModifier("INTEGRITY")
    def dotsIntegrity(self):
        output = []
        for i in range(self.integrity):
            output.append(True)
        for i in range(5 - self.integrity):
            output.append(False)
        return output
    investigation = DotField("Investigation")
    def abilityInvestigation(self):
        return self.investigation + self.effectModifier("INVESTIGATION")
    def dotsInvestigation(self):
        output = []
        for i in range(self.investigation):
            output.append(True)
        for i in range(5 - self.investigation):
            output.append(False)
        return output
    larceny = DotField("Larceny")
    def abilityLarceny(self):
        return self.larceny + self.effectModifier("LARCENY")
    def dotsLarceny(self):
        output = []
        for i in range(self.larceny):
            output.append(True)
        for i in range(5 - self.larceny):
            output.append(False)
        return output
    linguistics = DotField("Linguistics")
    def abilityLinguistics(self):
        return self.linguistics + self.effectModifier("LINGUISTICS")
    def dotsLinguistics(self):
        output = []
        for i in range(self.linguistics):
            output.append(True)
        for i in range(5 - self.linguistics):
            output.append(False)
        return output
    lore = DotField("Lore")
    def abilityLore(self):
        return self.lore + self.effectModifier("LORE")
    def dotsLore(self):
        output = []
        for i in range(self.lore):
            output.append(True)
        for i in range(5 - self.lore):
            output.append(False)
        return output
    martialArts = DotField("MartialArts")
    def abilityMartialArts(self):
        return self.martialArts + self.effectModifier("MARTIAL ARTS")
    def dotsMartialArts(self):
        output = []
        for i in range(self.martialArts):
            output.append(True)
        for i in range(5 - self.martialArts):
            output.append(False)
        return output
    medicine = DotField("Medicine")
    def abilityMedicine(self):
        return self.medicine + self.effectModifier("MEDICINE")
    def dotsMedicine(self):
        output = []
        for i in range(self.medicine):
            output.append(True)
        for i in range(5 - self.medicine):
            output.append(False)
        return output
    melee = DotField("Melee")
    def abilityMelee(self):
        return self.melee + self.effectModifier("MELEE")
    def dotsMelee(self):
        output = []
        for i in range(self.melee):
            output.append(True)
        for i in range(5 - self.melee):
            output.append(False)
        return output
    occult = DotField("Occult")
    def abilityOccult(self):
        return self.occult + self.effectModifier("OCCULT")
    def dotsOccult(self):
        output = []
        for i in range(self.occult):
            output.append(True)
        for i in range(5 - self.occult):
            output.append(False)
        return output
    performance = DotField("Performance")
    def abilityPerformance(self):
        return self.performance + self.effectModifier("PERFORMANCE")
    def dotsPerformance(self):
        output = []
        for i in range(self.performance):
            output.append(True)
        for i in range(5 - self.performance):
            output.append(False)
        return output
    presence = DotField("Presence")
    def abilityPresence(self):
        return self.presence + self.effectModifier("PRESENCE")
    def dotsPresence(self):
        output = []
        for i in range(self.presence):
            output.append(True)
        for i in range(5 - self.presence):
            output.append(False)
        return output
    resistance = DotField("Resistance")
    def abilityResistance(self):
        return self.resistance + self.effectModifier("RESISTANCE")
    def dotsResistance(self):
        output = []
        for i in range(self.resistance):
            output.append(True)
        for i in range(5 - self.resistance):
            output.append(False)
        return output
    ride = DotField("Ride")
    def abilityRide(self):
        return self.ride + self.effectModifier("RIDE")
    def dotsRide(self):
        output = []
        for i in range(self.ride):
            output.append(True)
        for i in range(5 - self.ride):
            output.append(False)
        return output
    sail = DotField("Sail")
    def abilitySail(self):
        return self.sail + self.effectModifier("SAIL")
    def dotsSail(self):
        output = []
        for i in range(self.sail):
            output.append(True)
        for i in range(5 - self.sail):
            output.append(False)
        return output
    socialize = DotField("Socialize")
    def abilitySocialize(self):
        return self.socialize + self.effectModifier("SOCIALIZE")
    def dotsSocialize(self):
        output = []
        for i in range(self.socialize):
            output.append(True)
        for i in range(5 - self.socialize):
            output.append(False)
        return output
    stealth = DotField("Stealth")
    def abilityStealth(self):
        return self.stealth + self.effectModifier("STEALTH")
    def dotsStealth(self):
        output = []
        for i in range(self.stealth):
            output.append(True)
        for i in range(5 - self.stealth):
            output.append(False)
        return output
    survival = DotField("Survival")
    def abilitySurvival(self):
        return self.survival + self.effectModifier("SURVIVAL")
    def dotsSurvival(self):
        output = []
        for i in range(self.survival):
            output.append(True)
        for i in range(5 - self.survival):
            output.append(False)
        return output
    thrown = DotField("Thrown")
    def abilityThrown(self):
        return self.thrown + self.effectModifier("THROWN")
    def dotsThrown(self):
        output = []
        for i in range(self.thrown):
            output.append(True)
        for i in range(5 - self.thrown):
            output.append(False)
        return output
    war = DotField("War")
    def abilityWar(self):
        return self.war + self.effectModifier("WAR")
    def dotsWar(self):
        output = []
        for i in range(self.war):
            output.append(True)
        for i in range(5 - self.war):
            output.append(False)
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

    #=========== WILLPOWER ============#
    willpowerCap = 10
    willpowerMax = NamedIntegerField("Maximum Willpower")
    willpower = NamedIntegerField("Current Willpower")

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
        return mod + ceil((self.attributeWits() + self.abilityIntegrity()) / 2) + self.effectModifier("RESOLVE")

    def guile(self, speciality=None, mod=0):
        return mod + ceil((self.attributeManipulation() + self.abilitySocialize()) / 2) + self.effectModifier("GUILE")

    def soakNatural(self, mod=0):
        return mod + self.attributeStamina() + self.effectModifier("SOAK NATURAL")

    def soakArmored(self, mod=0):
        return mod + self.armorSoak()

    def soakTotal(self, mod=0):
        return mod + self.soakNatural() + self.soakArmored()

    def hardness(self, mod=0):
        return mod + self.armorHardness() + self.effectModifier("HARDNESS")

    def joinBattle(self, mod=0):
        return mod + self.attributeWits() + self.abilityAwareness() + 3 + self.effectModifier("JOIN BATTLE")

    def evasion(self, mod=0):
        return mod + ceil((self.attributeDexterity() + self.abilityDodge()) / 2) - self.armorMobilityPenalty() + self.effectModifier("EVASION")

    def rush(self, mod=0):
        return mod + self.attributeDexterity() + self.abilityAthletics() + self.effectModifier("RUSH")

    def disengage(self, mod=0):
        return mod + self.attributeDexterity() + self.abilityDodge() + self.effectModifier("DISENGAGE")

class characterExaltBase(characterBase):
    anima = models.CharField(verbose_name="Anima", max_length=100)

    #============= MOTES ==============#
    motesPersonalMax = NamedIntegerField("Maximum Personal Motes")
    motesPersonal = NamedIntegerField("Current Personal Motes")
    motesPeripheralMax = NamedIntegerField("Maximum Peripheral Motes")
    motesPeripheral = NamedIntegerField("Current Peripheral Motes")

    #============= LIMIT ==============#
    limitTrigger = models.TextField(verbose_name="Limit Trigger", blank="False", max_length=1000)
    limitBreak = NamedIntegerField("Limit Break")

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

class characterMortal(characterBase):
    def type(self):
        return "Mortal"

class characterExaltSolar(characterExaltBase):
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

class characterExaltLunar(characterExaltBase):
    def type(self):
        return "Lunar Exalt"

    caste = SingleChoiceField("Lunar Caste", CASTES_LUNAR)
    #========= SHAPESHIFTING ==========#
    spiritShape = models.CharField(verbose_name="Spirit Shape", max_length=100)
    # Reverse relation
    def shapeSet(self):
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
class itemBase(PolymorphicModel):
    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()

class item(itemBase):
    pass

#==============================================================================#
#---------------------------------- WEAPONS -----------------------------------#
#==============================================================================#
class itemWeaponBase(itemBase):
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
    category = SingleChoiceField("Category", CATEGORIES)
    tags = MultiChoiceField("Tags", TAGS_ARMOR)
    soak = NamedIntegerField("Soak")
    hardness = NamedIntegerField("Hardness")
    mobilityPenalty = NamedIntegerField("Mobility Penalty")
    attunement = NamedIntegerField("Attunement")

#==============================================================================#
#---------------------------------- EFFECTS -----------------------------------#
#==============================================================================#

class effectBase(PolymorphicModel):
    def __str__(self):
        return self.name

    name = NameField()
    description = DescriptionField()
    rollConfiguration = NamedManyToManyField("Roll Configurations", rollConfiguration)
    modifiers = NamedManyToManyField("Modifiers", modifierBase)
    def modifier(self, keyword):
        output = 0
        for modifier in self.modifiers.all():
            if keyword == modifier.keyword:
                output += modifier.value
        return output

#==============================================================================#
#----------------------------------- CHARMS -----------------------------------#
#==============================================================================#
class charmBase(effectBase):
    levelEssence = NamedIntegerField("Essence Level")
    charmType = SingleChoiceField("Charm Type", CHARM_TYPES)
    duration = SingleChoiceField("Charm Duration", CHARM_DURATIONS)
    keywords = MultiChoiceField("Charm Keywords", CHARM_KEYWORDS)

class charmMartialArt(charmBase):
    levelKey = NamedIntegerField("Martial Arts Level")
    key = None

class charmEvocation(charmBase):
    levelKey = 0
    key = NamedForeignKeyField("Artifact", itemBase)

class charmSolar(charmBase):
    levelKey = NamedIntegerField("Ability Level")
    key = SingleChoiceField("Key Ability", ABILITIES)

class charmLunar(charmBase):
    levelKey = NamedIntegerField("Attribute Level")
    key = SingleChoiceField("Key Attribute", ATTRIBUTES)

class charmLunarShape(charmBase):
    levelKey = 0
    key = None

#==============================================================================#
#----------------------------------- MERITS -----------------------------------#
#==============================================================================#
class merit(effectBase):
    dots = DotField("Dots")

#==============================================================================#
#-------------------------------- SPECIALITIES --------------------------------#
#==============================================================================#
class speciality(effectBase):
    pass
#==============================================================================#
#--------------------------------- INTIMACIES ---------------------------------#
#==============================================================================#
class intimacyBase(PolymorphicModel):
    def __str__(self):
        return "[{}] {}".format(self.description, self.intensity)

    description = DescriptionField()
    intensity = SingleChoiceField("Intensity", INTENSITIES)

class intimacyTie(intimacyBase):
    target = NamedCharField("Target")

class intimacyPrincipal(intimacyBase):
    pass

#==============================================================================#
#--------------------------------- OWNERSHIP ----------------------------------#
#==============================================================================#
class ownershipBase(PolymorphicModel):
    notes = models.TextField(verbose_name="Notes", blank=True)
    active = NamedBooleanField("Active/Equipped?")

class ownershipCharacterBase(ownershipBase):
    owner = NamedForeignKeyField("Owner", characterBase)
class ownershipCharacterExaltBase(ownershipBase):
    owner = NamedForeignKeyField("Exalted Owner", characterExaltBase)
class ownershipCharacterExaltSolarBase(ownershipBase):
    owner = NamedForeignKeyField("Solar Exalted Owner", characterExaltSolar)
class ownershipCharacterExaltLunarBase(ownershipBase):
    owner = NamedForeignKeyField("Lunar Exalted Owner", characterExaltLunar)

class ownershipItem(ownershipCharacterBase):
    target = NamedForeignKeyField("Item", item)
class ownershipItemWeapon(ownershipCharacterBase):
    target = NamedForeignKeyField("Weapon", itemWeaponBase)
class ownershipItemArmor(ownershipCharacterBase):
    target = NamedForeignKeyField("Armor", itemArmor)

class ownershipCharmMartialArt(ownershipCharacterExaltBase):
    target = NamedForeignKeyField("Martial Arts Charm", characterExaltBase)
class ownershipCharmEvocation(ownershipCharacterExaltBase):
    target = NamedForeignKeyField("Evocation", characterExaltBase)
class ownershipCharmSolar(ownershipCharacterExaltSolarBase):
    target = NamedForeignKeyField("Solar Charm", characterExaltSolar)
class ownershipCharmLunar(ownershipCharacterExaltLunarBase):
    target = NamedForeignKeyField("Lunar Charm", characterExaltLunar)
class ownershipCharmLunarShape(ownershipCharacterExaltLunarBase):
    target = NamedForeignKeyField("Lunar Shape", characterExaltLunar)

class ownershipMerit(ownershipCharacterBase):
    target = NamedForeignKeyField("Merit", merit)

class ownershipSpeciality(ownershipCharacterBase):
    target = NamedForeignKeyField("Speciality", speciality)

class ownershipIntimacyTie(ownershipCharacterBase):
    target = NamedForeignKeyField("Tie", intimacyTie)
class ownershipIntimacyPrincipal(ownershipCharacterBase):
    target = NamedForeignKeyField("Principal", intimacyPrincipal)
