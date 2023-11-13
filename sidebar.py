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

def iron_mine(iron_mine):
    lvl = str(iron_mine.lvl)
    name = "Eisen Mine"
    villagename = iron_mine.village.name
    color = iron_mine.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_iron_mine", 7))

    return content

def cabin(cabin):
    lvl = str(cabin.lvl)
    name = "Holzhütte"
    villagename = cabin.village.name
    color = cabin.owner.color
    content = []
    content.append(buttons.Txt(name, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(villagename, 800, 740, color, 16))
    content.append(buttons.Button("upgrade_cabin", 7))

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
    if field.buildings == [] and field.typ != "water":
        content.append(buttons.Button("add_village", 7))
    if field.typ == "mountain" and field.test_for_village(d, owner) == True: # More efficient version possible
        testermine = False
        testerironmine = False
        for i in field.buildings:  
            if i.typ == "mine":
                content.append(buttons.Button("upgrade_mine", 6))
                testermine = True
        if testermine == False:
            content.append(buttons.Button("add_mine", 6))
        for i in field.buildings:  
            if i.typ == "iron_mine":
                content.append(buttons.Button("upgrade_iron_mine", 5))
                testerironmine = True
        if testerironmine == False:
            content.append(buttons.Button("add_iron_mine", 5))
    if field.typ == "forest" and field.test_for_village(d, owner) == True:
        testercabin = False
        for i in field.buildings:  
            if i.typ == "cabin":
                content.append(buttons.Button("upgrade_cabin", 6))
                testercabin = True
        if testercabin == False:
            content.append(buttons.Button("add_cabin", 6))

    return content

def investigationstree():
    content = []
    content.append(buttons.Button("open_it_productions", 8))

    return content

def open_it_productions():
    content = []
    content.append(buttons.Button("open_t_quarry", 8))

    return content

def open_t_quarry():
    content = []
    content.append(buttons.Txt("Quarry", 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Button("investigate_quarry"), 1)

    return content