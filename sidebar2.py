import arcade
import buttons2 as buttons

def entities():
    content = []
    content.append(buttons.Button("recruit_soldier", (1, 8)))

    return content

def start(player):
    playername = player.name
    color = player.color
    content = []
    content.append(buttons.Txt(playername,0, 0, color, 20, True))
    content.append(buttons.Button("open_investigations", (1, 8)))
    content.append(buttons.Button("pass_turn", (1, 1)))

    return content

def entity(entity):
    typ = entity.typ
    ownername = entity.owner.name
    color = entity.owner.color
    health = str(entity.health)
    damage = str(entity.damage)
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(typ, 0, 0, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt(ownername, 0, 30, color, 16))
    content.append(buttons.Txt(health, 150, 0, arcade.color.DARK_MOSS_GREEN, 16, True))
    content.append(buttons.Txt(damage, 0, 60, arcade.color.RED, 16))
    content.append(buttons.Txt("damage", 20, 60, arcade.color.BLACK, 16))

    return content

def quarry(quarry):
    lvl = str(quarry.lvl)
    name = "Quarry"
    villagename = quarry.village.name
    color = quarry.owner.color
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(name, 0, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 150, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 0, 60, color, 16))
    faktor = round(quarry.lvl/2 + 0.1)
    content.append(buttons.Txt("Cost:", 0, 108, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(5*faktor) + " stone", 0, 128, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(2*faktor) + " wood", 0, 148, arcade.color.BLACK, 16))
    content.append(buttons.Button("upgrade_quarry", (1, 8)))

    return content

def mine(mine):
    lvl = str(mine.lvl)
    name = "Mine"
    villagename = mine.village.name
    color = mine.owner.color
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(name, 0, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 150, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 0, 60, color, 16))
    faktor = round(mine.lvl/2 + 0.1)
    content.append(buttons.Txt("Cost:", 0, 108, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(5*faktor) + " iron", 0, 128, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(2*faktor) + " stone", 0, 148, arcade.color.BLACK, 16))
    content.append(buttons.Button("upgrade_mine", (1, 8)))

    return content

def cabin(cabin):
    lvl = str(cabin.lvl)
    name = "Cabin"
    villagename = cabin.village.name
    color = cabin.owner.color
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(name, 0, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 150, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 0, 60, color, 16))
    faktor = round(cabin.lvl/2 + 0.1)
    content.append(buttons.Txt("Cost:", 0, 108, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(5*faktor) + " wood", 0, 128, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(2*faktor) + " wool", 0, 148, arcade.color.BLACK, 16))
    content.append(buttons.Button("upgrade_cabin", (1, 8)))

    return content

def wheat_plot(wheat_plot):
    lvl = str(wheat_plot.lvl)
    name = "Wheat plot"
    villagename = wheat_plot.village.name
    color = wheat_plot.owner.color
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(name, 0, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 150, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 0, 60, color, 16))
    faktor = round(wheat_plot.lvl/2 + 0.1)
    content.append(buttons.Txt("Cost:", 0, 108, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(5*faktor) + " wheat", 0, 128, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(2*faktor) + " iron", 0, 148, arcade.color.BLACK, 16))
    content.append(buttons.Button("upgrade_wheat_plot", (1, 8)))

    return content

def pasture(pasture):
    lvl = str(pasture.lvl)
    name = "Pasture"
    villagename = pasture.village.name
    color = pasture.owner.color
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(name, 0, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 150, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 60, color, 16))
    faktor = round(pasture.lvl/2 + 0.1)
    content.append(buttons.Txt("Cost:", 0, 108, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(5*faktor) + " wool", 0, 128, arcade.color.BLACK, 16))
    content.append(buttons.Txt(str(2*faktor) + " wheat", 0, 148, arcade.color.BLACK, 16))
    content.append(buttons.Button("upgrade_pasture", (1, 8)))

    return content

def village(village):
    lvl = str(village.lvl)
    name = village.name
    ownername = village.owner.name
    color = village.owner.color
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Txt(name, 0, 40, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt(lvl, 150, 40, arcade.color.BLACK, 20))
    content.append(buttons.Txt(ownername, 800, 0, color, 16))
    content.append(buttons.Button("recruit", (1, 8)))

    return content

def field(field, d, owner):
    name = field.typ
    if name == "mountain":
        name = "Mountain"
    elif name == "forest":
        name = "Forest"
    elif name == "water":
        name = "Sea"
    elif name == "grass":
        name = "Grass"
    content = []
    content.append(buttons.Button("home", (1,1)))
    content.append(buttons.Txt(name, -22, 730, arcade.color.BLACK, 20, True))
    if field.buildings == []:                                                    # Create Buttons for adding buildings
        if field.typ != "water" and field.typ != "mountain" and field.typ != "forest" and field.test_for_village(d, owner) == False:
            content.append(buttons.Button("add_village", (1, 8)))
        if field.typ == "forest" and field.test_for_village(d, owner) == True and owner.technologies["cabin"] == True:
            content.append(buttons.Button("add_cabin", 7))
            content.append(buttons.Txt("Cost:", 0, 514, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 0, 494, arcade.color.BLACK, 16))
        if field.typ == "mountain" and field.test_for_village(d, owner) == True and owner.technologies["quarry"] == True:
            content.append(buttons.Button("add_quarry", (1, 7)))
            content.append(buttons.Txt("Cost:", 0, 514, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 0, 494, arcade.color.BLACK, 16))
        if field.typ == "mountain" and field.test_for_village(d, owner) == True and owner.technologies["mine"] == True:   
            content.append(buttons.Button("add_mine", (1, 5)))
            content.append(buttons.Txt("Cost:", 0, 345, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 0, 325, arcade.color.BLACK, 16))
        if field.typ == "grass" and field.test_for_village(d, owner) == True and owner.technologies["pasture"] == True:
            content.append(buttons.Button("add_pasture", (1, 7)))
            content.append(buttons.Txt("Cost:", 0, 514, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 0, 494, arcade.color.BLACK, 16))
        if field.typ == "grass" and field.test_for_village(d, owner) == True and owner.technologies["wheat_plot"] == True:
            content.append(buttons.Button("add_wheat_plot", (1, 5)))
            content.append(buttons.Txt("Cost:", 0, 345, arcade.color.BLACK, 16))
            content.append(buttons.Txt("25 coins", 0, 325, arcade.color.BLACK, 16))
    else:                                                                         # Create Buttons to upgrade existing buildings from the field sb
        if field.buildings[0].typ == "cabin":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_cabin", (1, 8)))
            content.append(buttons.Txt("Cost:", 0, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " wood", 0, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " wool", 0, 552, arcade.color.BLACK, 16))
        elif field.buildings[0].typ == "quarry":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_quarry", (1, 8)))
            content.append(buttons.Txt("Cost:", 0, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " stone", 0, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " wood", 0, 552, arcade.color.BLACK, 16))
        elif field.buildings[0].typ == "mine":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_mine", (1, 8)))
            content.append(buttons.Txt("Cost:", 0, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " iron", 0, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " stone", 0, 552, arcade.color.BLACK, 16))
        elif field.buildings[0].typ == "pasture":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_pasture", (1, 8)))
            content.append(buttons.Txt("Cost:", 0, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " wool", 0, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " wheat", 0, 552, arcade.color.BLACK, 16))
        elif field.buildings[0].typ == "wheat_plot":
            faktor = round(field.buildings[0].lvl/2 + 0.1)
            content.append(buttons.Button("upgrade_wheat_plot", (1, 8)))
            content.append(buttons.Txt("Cost:", 0, 592, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(5*faktor) + " wheat", 0, 572, arcade.color.BLACK, 16))
            content.append(buttons.Txt(str(2*faktor) + " iron", 0, 552, arcade.color.BLACK, 16))



    return content

#  Investigations

def investigationstree():
    content = []
    content.append(buttons.Button("home", (1, 1)))
    content.append(buttons.Button("open_it_productions", (1, 8)))

    return content

def open_it_productions(player):
    content = []
    content.append(buttons.Button("home", (1, 9)))
    if player.technologies["quarry"] != True:
        content.append(buttons.Button("open_t_quarry", (1, 8)))
    elif player.technologies["quarry"] == True:
        content.append(buttons.Button("researched_t_quarry", (1, 8))) # No f needed but for img
    if player.technologies["cabin"] != True:
        content.append(buttons.Button("open_t_cabin", (1, 7)))
    elif player.technologies["cabin"] == True:
        content.append(buttons.Button("researched_t_cabin", (1, 7)))
    if player.technologies["wheat_plot"] != True:
        content.append(buttons.Button("open_t_wheat_plot", (1, 6)))
    elif player.technologies["wheat_plot"] == True:
        content.append(buttons.Button("researched_t_wheat_plot", (1, 6)))
    if player.technologies["pasture"] != True:
        content.append(buttons.Button("open_t_pasture", (1, 5)))
    elif player.technologies["pasture"] == True:
        content.append(buttons.Button("researched_t_pasture", (1, 5)))
    if player.technologies["mine"] != True:
        content.append(buttons.Button("open_t_mine", (1, 4)))
    elif player.technologies["mine"] == True:
        content.append(buttons.Button("researched_t_mine", (1, 4)))

    return content

def open_t_quarry():
    content = []
    content.append(buttons.Button("home", (1, 9)))
    content.append(buttons.Txt("Quarry", 0, 676, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt("Produces stone", 800, 651, arcade.color.BLACK, 16))
    content.append(buttons.Txt("Cost:", 0, 531, arcade.color.BLACK, 16))
    content.append(buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16))
    content.append(buttons.Button("investigate_quarry", (1, 1)))

    return content

def open_t_cabin():
    content = []
    content.append(buttons.Button("home", (1, 9)))
    content.append(buttons.Txt("Cabin", 0, 676, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt("Produces wood", 800, 651, arcade.color.BLACK, 16))
    content.append(buttons.Txt("Cost:", 0, 531, arcade.color.BLACK, 16))
    content.append(buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16))
    content.append(buttons.Button("investigate_cabin", (1, 1)))

    return content

def open_t_wheat_plot():
    content = []
    content.append(buttons.Button("home", (1, 9)))
    content.append(buttons.Txt("Wheat Plot", 0, 676, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt("Produces wheat", 800, 651, arcade.color.BLACK, 16))
    content.append(buttons.Txt("Cost:", 0, 531, arcade.color.BLACK, 16))
    content.append(buttons.Txt("1 investigationpoint", 800, 511, arcade.color.BLACK, 16))
    content.append(buttons.Button("investigate_wheat_plot", (1, 1)))

    return content

def open_t_pasture():
    content = []
    content.append(buttons.Button("home", (1, 9)))
    content.append(buttons.Txt("Pasture", 0, 676, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt("Produces wool", 0, 651, arcade.color.BLACK, 16))
    content.append(buttons.Txt("Cost:", 0, 531, arcade.color.BLACK, 16))
    content.append(buttons.Txt("1 investigationpoint", 0, 511, arcade.color.BLACK, 16))
    content.append(buttons.Button("investigate_pasture", (1, 1)))

    return content

def open_t_mine():
    content = []
    content.append(buttons.Button("home", (1, 9)))
    content.append(buttons.Txt("Mine", 0, 676, arcade.color.BLACK, 20, True))
    content.append(buttons.Txt("Produces iron", 0, 651, arcade.color.BLACK, 16))
    content.append(buttons.Txt("Cost:", 0, 531, arcade.color.BLACK, 16))
    content.append(buttons.Txt("1 investigationpoint", 0, 511, arcade.color.BLACK, 16))
    content.append(buttons.Button("investigate_mine", (1, 1)))

    return content