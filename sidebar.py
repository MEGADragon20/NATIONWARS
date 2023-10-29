import arcade
import buttons

def start():
    content = []
    content.append(buttons.Button("open_investigations", 8))

    return content

def entity(entity):
    typ = entity.typ
    ownername = entity.owner.name
    color = entity.owner.color
    health = entity.health
    damage = entity.damage
    content = []
    content.append(buttons.Txt(typ, 800, 760, arcade.color.BLACK, 20))
    content.append(buttons.Txt(ownername, 800, 760, color, 20))
    content.append(buttons.Txt(health, 950, 760, arcade.color.BLACK, 16))
    content.append(buttons.Txt(damage, 800, 740, arcade.color.BLACK, 20))
    content.append(buttons.Txt("damage", 820, 740, arcade.color.BLACK, 20))

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

def field(field):
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

    return content