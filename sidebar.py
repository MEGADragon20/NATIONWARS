import arcade
import buttons
from instances import Instances

def entities_l():
    return [
        buttons.Button("recruit_helicopter", 4),
        buttons.Button("recruit_reconsys", 6),
        buttons.Button("recruit_recon", 7),
        buttons.Button("recruit_soldier", 8),
        buttons.Button("home", 9)
    ]

def entities_w():
    return [

        buttons.Button("recruit_corvette", 4),
        buttons.Button("home", 9)
    ]


def start(player):s
    return [
        buttons.Txt(player.name,800, 760, player.color, 20, True),
        buttons.Button("open_investigations", 8),
        buttons.Button("pass_turn", 1)
    ]


def entity(entity, Village):
    for building in Instances.game.buildings:
        if isinstance(building, Village) and arcade.check_for_collision(building, Instances.game.fields[Instances.game.activefield]):
            return [
                buttons.Button("home", 1),
                buttons.Txt(entity.typ, 800, 760, arcade.color.BLACK, 20, True),
                buttons.Txt(entity.owner.name, 800, 730, entity.owner.color, 16),
                buttons.Txt(str(entity.health), 950, 760, arcade.color.DARK_MOSS_GREEN, 16, True),
                buttons.Txt(str(entity.damage), 800, 700, arcade.color.RED, 16),
                buttons.Txt("damage", 820, 700, arcade.color.BLACK, 16),
                buttons.Button("takeover", 8)
            ]
    return [
        buttons.Button("home", 1),
        buttons.Txt(entity.typ, 800, 760, arcade.color.BLACK, 20, True),
        buttons.Txt(entity.owner.name, 800, 730, entity.owner.color, 16),
        buttons.Txt(str(entity.health), 950, 760, arcade.color.DARK_MOSS_GREEN, 16, True),
        buttons.Txt(str(entity.damage), 800, 700, arcade.color.RED, 16),
        buttons.Txt("damage", 820, 700, arcade.color.BLACK, 16),
        buttons.Img("data/entities/" + entity.typ + ".png", 890, 500, 4)
        ]


def quarry(quarry):
    faktor = round(quarry.lvl/2 + 0.1)
    return [
        buttons.Button("home", 1),
        buttons.Txt("Quarry", 800, 760, arcade.color.BLACK, 20),
        buttons.Txt(str(quarry.lvl), 950, 760, arcade.color.BLACK, 20),
        buttons.Txt(quarry.village.name, 800, 740, quarry.owner.color, 16),
        buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16),
        buttons.Txt(str(5*faktor) + " stone", 800, 572, arcade.color.BLACK, 16),
        buttons.Txt(str(2*faktor) + " wood", 800, 552, arcade.color.BLACK, 16),
        buttons.Button("upgrade_quarry", 8)
    ]


def mine(mine):
    faktor = round(mine.lvl/2 + 0.1)
    return [
        buttons.Button("home", 1),
        buttons.Txt("Mine", 800, 760, arcade.color.BLACK, 20),
        buttons.Txt(str(mine.lvl), 950, 760, arcade.color.BLACK, 20),
        buttons.Txt(mine.village.name, 800, 740, mine.owner.color, 16),
        buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16),
        buttons.Txt(str(5*faktor) + " iron", 800, 572, arcade.color.BLACK, 16),
        buttons.Txt(str(2*faktor) + " stone", 800, 552, arcade.color.BLACK, 16),
        buttons.Button("upgrade_mine", 8)
    ]


def cabin(cabin):
    faktor = round(cabin.lvl/2 + 0.1)
    return [
        buttons.Button("home", 1),
        buttons.Txt("Cabin", 800, 760, arcade.color.BLACK, 20),
        buttons.Txt(str(cabin.lvl), 950, 760, arcade.color.BLACK, 20),
        buttons.Txt(cabin.village.name, 800, 740, cabin.owner.color, 16),
        buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16),
        buttons.Txt(str(5*faktor) + " wood", 800, 572, arcade.color.BLACK, 16),
        buttons.Txt(str(2*faktor) + " wool", 800, 552, arcade.color.BLACK, 16),
        buttons.Button("upgrade_cabin", 8)
    ]


def wheat_plot(wheat_plot):
    faktor = round(wheat_plot.lvl/2 + 0.1)
    return [
        buttons.Button("home", 1),
        buttons.Txt("Wheat plot", 800, 760, arcade.color.BLACK, 20),
        buttons.Txt(str(wheat_plot.lvl), 950, 760, arcade.color.BLACK, 20),
        buttons.Txt(wheat_plot.village.name, 800, 740, wheat_plot.owner.color, 16),
        buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16),
        buttons.Txt(str(5*faktor) + " wheat", 800, 572, arcade.color.BLACK, 16),
        buttons.Txt(str(2*faktor) + " iron", 800, 552, arcade.color.BLACK, 16),
        buttons.Button("upgrade_wheat_plot", 8)
    ]


def pasture(pasture):
    faktor = round(pasture.lvl/2 + 0.1)
    return [
        buttons.Button("home", 1),
        buttons.Txt("Pasture", 800, 760, arcade.color.BLACK, 20),
        buttons.Txt(str(pasture.lvl), 950, 760, arcade.color.BLACK, 20),
        buttons.Txt(pasture.village.name, 800, 740, pasture.owner.color, 16),
        buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16),
        buttons.Txt(str(5*faktor) + " wool", 800, 572, arcade.color.BLACK, 16),
        buttons.Txt(str(2*faktor) + " wheat", 800, 552, arcade.color.BLACK, 16),
        buttons.Button("upgrade_pasture", 8)
    ]


def village(village, player):
    content = [
        buttons.Button("home", 1),
        buttons.Txt(village.name, 800, 760, arcade.color.BLACK, 20, True),
        buttons.Txt(str(village.lvl), 950, 760, arcade.color.BLACK, 20),
        buttons.Txt(village.owner.name, 800, 740, village.owner.color, 16)
    ]
    if player == village.owner:
        content.append(buttons.Button("recruit_village", 7))

    return content

def naval_base(naval_base):
    content = [
        buttons.Button("home",1),
        buttons.Txt("Naval_Base", 800, 760, arcade.color.BLACK, 20),
        buttons.Txt(str(naval_base.lvl), 950, 760, arcade.color.BLACK, 20)
    ]
    
    content.append(buttons.Button("recruit_naval_base", 7))
    return content

def field(field, d, owner):
    name = field.typ.capitalize()
    if name == "Water":
        name = "Sea"
    content = [
        buttons.Button("home", 1),
        buttons.Txt(name, 800, 760, arcade.color.BLACK, 20, True)
    ]

    if field.buildings == []:                                                    # Create Buttons for adding buildings
        if  not field.typ in {"water", "mountain", "forest"} \
        and field.test_for_village(d, owner) == False \
        and not owner.turnstovillage:
            content.append(buttons.Button("add_village", 8))

        if  field.typ == "forest" \
        and field.test_for_village(d, owner) == True \
        and owner.technologies["cabin"] == True \
        and field.neighbor_for_village(d, owner).owner == owner:
            content.append(buttons.Button("add_cabin", 7))
            content.append(buttons.Txt("Cost:", 800, 514, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 800, 494, arcade.color.BLACK, 16))

        if  field.typ == "mountain" \
        and field.test_for_village(d, owner) == True \
        and owner.technologies["quarry"] == True \
        and field.neighbor_for_village(d, owner).owner == owner:
            content.append(buttons.Button("add_quarry", 7))
            content.append(buttons.Txt("Cost:", 800, 514, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 800, 494, arcade.color.BLACK, 16))

        if  field.typ == "mountain" \
        and field.test_for_village(d, owner) == True \
        and owner.technologies["mine"] == True \
        and field.neighbor_for_village(d, owner).owner == owner:   
            content.append(buttons.Button("add_mine", 5))
            content.append(buttons.Txt("Cost:", 800, 345, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 800, 325, arcade.color.BLACK, 16))

        if  field.typ == "grass" \
        and field.test_for_village(d, owner) == True \
        and owner.technologies["pasture"] == True \
        and field.neighbor_for_village(d, owner).owner == owner:
            content.append(buttons.Button("add_pasture", 7))
            content.append(buttons.Txt("Cost:", 800, 514, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 800, 494, arcade.color.BLACK, 16))

        if  field.typ == "grass" \
        and field.test_for_village(d, owner) == True \
        and owner.technologies["wheat_plot"] == True \
        and field.neighbor_for_village(d, owner).owner == owner:
            content.append(buttons.Button("add_wheat_plot", 5))
            content.append(buttons.Txt("Cost:", 800, 345, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 800, 325, arcade.color.BLACK, 16))

        if field.typ == "water":
            content.append(buttons.Button("add_naval_base", 5))
            content.append(buttons.Txt("Cost:", 800, 345, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 800, 325, arcade.color.BLACK, 16))  

    else:                                                                         # Create Buttons to upgrade existing buildings from the field sb
        if field.buildings[0].typ == "cabin":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_cabin", 8))
            content.append(buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " wood", 800, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " wool", 800, 552, arcade.color.BLACK, 16))

        elif field.buildings[0].typ == "quarry":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_quarry", 8))
            content.append(buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " stone", 800, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " wood", 800, 552, arcade.color.BLACK, 16))

        elif field.buildings[0].typ == "mine":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_mine", 8))
            content.append(buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " iron", 800, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " stone", 800, 552, arcade.color.BLACK, 16))

        elif field.buildings[0].typ == "pasture":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_pasture", 8))
            content.append(buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " wool", 800, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " wheat", 800, 552, arcade.color.BLACK, 16))

        elif field.buildings[0].typ == "wheat_plot":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_wheat_plot", 8))
            content.append(buttons.Txt("Cost:", 800, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " wheat", 800, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " iron", 800, 552, arcade.color.BLACK, 16))

    return content


#  Investigations


def investigationstree():
    return [
        buttons.Button("home", 9),
        buttons.Button("open_it_productions", 8)
    ]


def open_it_productions(player):
    content = [
        buttons.Button("home", 9)
    ]

    if player.technologies["quarry"] != True:
        content.append(buttons.Button("open_t_quarry", 8))
    elif player.technologies["quarry"] == True:
        content.append(buttons.Button("researched_t_quarry", 8)) # No f needed but for img
    if player.technologies["cabin"] != True:
        content.append(buttons.Button("open_t_cabin", 7))
    elif player.technologies["cabin"] == True:
        content.append(buttons.Button("researched_t_cabin", 7))
    if player.technologies["wheat_plot"] != True:
        content.append(buttons.Button("open_t_wheat_plot", 6))
    elif player.technologies["wheat_plot"] == True:
        content.append(buttons.Button("researched_t_wheat_plot", 6))
    if player.technologies["pasture"] != True:
        content.append(buttons.Button("open_t_pasture", 5))
    elif player.technologies["pasture"] == True:
        content.append(buttons.Button("researched_t_pasture", 5))
    if player.technologies["mine"] != True:
        content.append(buttons.Button("open_t_mine", 4))
    elif player.technologies["mine"] == True:
        content.append(buttons.Button("researched_t_mine", 4))

    return content


def open_t_quarry():
    content = [
        buttons.Button("home", 9),
        buttons.Txt("Quarry", 800, 676, arcade.color.BLACK, 20, True),
        buttons.Txt("Produces stone", 800, 651, arcade.color.BLACK, 16),
        buttons.Txt("Cost:", 800, 531, arcade.color.BLACK, 16),
        buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16),
        buttons.Button("investigate_quarry", 1)
    ]

    return content


def open_t_cabin():
    return [
        buttons.Button("home", 9),
        buttons.Txt("Cabin", 800, 676, arcade.color.BLACK, 20, True),
        buttons.Txt("Produces wood", 800, 651, arcade.color.BLACK, 16),
        buttons.Txt("Cost:", 800, 531, arcade.color.BLACK, 16),
        buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16),
        buttons.Button("investigate_cabin", 1)
    ]


def open_t_wheat_plot():
    return [
        buttons.Button("home", 9),
        buttons.Txt("Wheat Plot", 800, 676, arcade.color.BLACK, 20, True),
        buttons.Txt("Produces wheat", 800, 651, arcade.color.BLACK, 16),
        buttons.Txt("Cost:", 800, 531, arcade.color.BLACK, 16),
        buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16),
        buttons.Button("investigate_wheat_plot", 1)
    ]


def open_t_pasture():
    return [
        buttons.Button("home", 9),
        buttons.Txt("Pasture", 800, 676, arcade.color.BLACK, 20, True),
        buttons.Txt("Produces wool", 800, 651, arcade.color.BLACK, 16),
        buttons.Txt("Cost:", 800, 531, arcade.color.BLACK, 16),
        buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16),
        buttons.Button("investigate_pasture", 1)
    ]


def open_t_mine():
    return [
        buttons.Button("home", 9),
        buttons.Txt("Mine", 800, 676, arcade.color.BLACK, 20, True),
        buttons.Txt("Produces iron", 800, 651, arcade.color.BLACK, 16),
        buttons.Txt("Cost:", 800, 531, arcade.color.BLACK, 16),
        buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16),
        buttons.Button("investigate_mine", 1)
    ]
