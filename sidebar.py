import arcade
import buttons

def start():
    content = []
    content.append(buttons.Button("open_investigations", 8))
    content.append(buttons.Button("pass_turn", 1))

    return content

def entity(entity):
    typ = entity.typ
    ownername = entity.owner.name
    color = entity.owner.color
    health = str(entity.health)
    damage = str(entity.damage)
    content = []
    content.append(buttons.Txt(typ, 800, 760, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt(ownername, 800, 730, color, 16))
    content.append(buttons.Txt(health, 950, 760, arcade.color.DARK_MOSS_GREEN, 16, True))
    content.append(buttons.Txt(damage, 800, 700, arcade.color.RED, 16))
    content.append(buttons.Txt("damage", 820, 700, arcade.color.BLACK, 16))

    return content

def quarry(quarry):
    lvl = str(quarry.lvl)
    name = "Quarry"
    villagename = quarry.village.name
    color = quarry.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_quarry", 7))

    return content

def mine(mine):
    lvl = str(mine.lvl)
    name = "Mine"
    villagename = mine.village.name
    color = mine.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_mine", 7))

    return content

def cabin(cabin):
    lvl = str(cabin.lvl)
    name = "Cabin"
    villagename = cabin.village.name
    color = cabin.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_cabin", 7))

    return content

def wheat_plot(wheat_plot):
    lvl = str(wheat_plot.lvl)
    name = "Wheat plot"
    villagename = wheat_plot.village.name
    color = wheat_plot.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_wheat_plot", 7))

    return content

def pasture(pasture):
    lvl = str(pasture.lvl)
    name = "Pasture"
    villagename = pasture.village.name
    color = pasture.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_pasture", 6))

    return content

def village(village):
    lvl = str(village.lvl)
    name = village.name
    ownername = village.owner.name
    color = village.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(ownername, 800, 740, color, 16))

    return content

def field(field, d, owner):
    name = field.typ
    if name == "mountain":
        name = "Berg"
    elif name == "forest":
        name = "Wald"
    elif name == "water":
        name = "Wasser"
    elif name == "grass":
        name = "Wiese"
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    if field.buildings == []:                                                    # Create Buttons for adding buildings
        if field.typ != "water" and field.test_for_village(d, owner) == False:
            content.append(buttons.Button("add_village", 8))
        if field.typ == "forest" and field.test_for_village(d, owner) == True and owner.technologies["cabin"] == True:
            content.append(buttons.Button("add_cabin", 7))
        if field.typ == "mountain" and field.test_for_village(d, owner) == True and owner.technologies["quarry"] == True:
            content.append(buttons.Button("add_quarry", 7))
        if field.typ == "mountain" and field.test_for_village(d, owner) == True and owner.technologies["mine"] == True:   
            content.append(buttons.Button("add_mine", 6))
        if field.typ == "grass" and field.test_for_village(d, owner) == True and owner.technologies["pasture"] == True:
            content.append(buttons.Button("add_pasture", 7))
        if field.typ == "grass" and field.test_for_village(d, owner) == True and owner.technologies["wheat_plot"] == True:
            content.append(buttons.Button("add_wheat_plot", 6))
    else:                                                                         # Create Buttons to upgrade existing buildings from the field sb
        if field.buildings[0].typ == "cabin":
            content.append(buttons.Button("upgrade_cabin", 8))
        elif field.buildings[0].typ == "quarry":
            content.append(buttons.Button("upgrade_quarry", 8))
        elif field.buildings[0].typ == "mine":
            content.append(buttons.Button("upgrade_mine", 8))
        elif field.buildings[0].typ == "pasture":
            content.append(buttons.Button("upgrade_pasture", 8))
        elif field.buildings[0].typ == "wheat_plot":
            content.append(buttons.Button("upgrade_wheat_plot", 8))



    return content

#  Investigations

def investigationstree():
    content = []
    content.append(buttons.Button("open_it_productions", 8))

    return content

def open_it_productions(player):
    content = []
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
    content = []
    content.append(buttons.Txt("Quarry", 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Button("investigate_quarry", 1))

    return content

def open_t_cabin():
    content = []
    content.append(buttons.Txt("Cabin", 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Button("investigate_cabin", 1))

    return content

def open_t_wheat_plot():
    content = []
    content.append(buttons.Txt("Wheat Plot", 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Button("investigate_wheat_plot", 1))

    return content

def open_t_pasture():
    content = []
    content.append(buttons.Txt("Pasture", 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Button("investigate_pasture", 1))

    return content

def open_t_mine():
    content = []
    content.append(buttons.Txt("Mine", 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Button("investigate_mine", 1))

    return content