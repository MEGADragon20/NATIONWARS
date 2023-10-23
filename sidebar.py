import arcade

def village(village):
    lvl = str(village.lvl)
    name = village.name
    ownername = village.owner.name
    color = village.owner.color
    content = []
    content.append(arcade.Text(name, 800, 760, arcade.color.BLACK, 20))
    content.append(arcade.Text(lvl, 950, 760, arcade.color.BLACK, 20))
    content.append(arcade.Text(ownername, 800, 740, color, 16))

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
    content.append(arcade.Text(name, 800, 760, arcade.color.BLACK, 20))

    return content