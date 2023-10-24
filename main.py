import arcade, random as r, arcade.gui
import reader, sidebar  


class Suchspiel(arcade.Window):
    def __init__(self, breite, höhe, titel, feld_h, feld_b):
        super().__init__(breite, höhe, titel)
        arcade.set_background_color((111,111,111)) 
        self.fields = arcade.SpriteList()
        self.buildings = arcade.SpriteList()
        self.entities = arcade.SpriteList()
        self.players = []
        self.sidebar = []
        self.Dictionary = {}
        index = 0
        for h in range(feld_h):
            for b in range(feld_b):
                a = reader.getvars()[index]
                self.Dictionary[(b, h)] =  Field(x = 32 + b*32, y = 32 + h*32, typ = a)
                self.fields.append(self.Dictionary[(b, h)])
                index += 1


        self.active = Field(x = 0, y = 0, typ = "grass")
        self.players.append(Player("Markus Söder", arcade.color.RED_DEVIL, "Conquerus"))
        self.entities.append(Soldier(32, 32, self.players[0]))
        self.buildings.append(self.fields[98].add_village("München", self.players[0])) 
        self.buildings.append(self.fields[99].add_mine(self.Dictionary, None))
        self.buildings.append(self.fields[387].add_village("Berlin", self.players[0])) 
        self.buildings.append(self.fields[386].add_mine(self.Dictionary, None)) 


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(1,1), (0,1), (0,0), (1,0)])
        if button == 1:
            for i in self.fields:
                if arcade.check_for_collision(pseudosprite, i):
                    self.active = i.select(self.Dictionary, self.fields, self.active)
                    self.sidebar.clear()
                    a = i.klick()
                    for i in a:
                        self.sidebar.append(i)
                
            for i in self.buildings:
                if arcade.check_for_collision(pseudosprite, i):
                    self.sidebar.clear()
                    a = i.klick()
                    for i in a:
                        self.sidebar.append(i)


        elif button == 2 or button == 4:
            for i in self.fields:
                if arcade.check_for_collision(pseudosprite, i):
                    pass

    def on_draw(self):
        self.clear()
        self.fields.draw()  
        self.buildings.draw()
        self.entities.draw()
        for i in self.sidebar:
            i.draw()
       


class Field(arcade.Sprite):
    def __init__(self,  x, y, typ):
        super().__init__("data/fields/" + typ + ".png", center_x = x, center_y = y)
        self.x = x
        self.y = y
        self.typ = typ
        self.pos = (((self.x - 32)/32),((self.y - 32)/ 32))
        self.buildings = []
        self.entities = []
    
    def select(self, f_dict, f_list, active):
        active.texture = arcade.load_texture("data/fields/" + active.typ + ".png")
        self.texture = arcade.load_texture("data/fields/active/" + self.typ + ".png")
        return self
    
    def klick(self):
        return sidebar.field(self)
    
# Add buildings
    def add_village(self, name, owner):
        a = Village(self.x, self.y, name, 1, owner)
        self.buildings.append(a) 
        return a
    
    def add_mine(self, d, owner):
        if self.typ != "mountain":
            raise(TypeError)
        a, b = self.pos
        if (a + 1, b) in d:
            if d[(a + 1, b)].buildings != []:
                if d[(a + 1, b)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a + 1, b)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a, b + 1) in d:
            if d[(a, b + 1)].buildings != []:
                if d[(a, b + 1)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a, b + 1)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a - 1 , b) in d:
            if d[(a - 1, b)].buildings != []:
                if d[(a - 1, b)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a - 1, b)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a, b - 1) in d:
            if d[(a, b - 1)].buildings != []:
                if d[(a, b - 1)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a, b - 1)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a + 1, b + 1) in d:
            if d[(a + 1, b + 1)].buildings != []:
                if d[(a + 1, b + 1)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a + 1, b + 1)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a - 1 , b - 1) in d:
            if d[(a - 1, b - 1)].buildings != []:
                if d[(a - 1, b - 1)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a - 1, b - 1)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a - 1, b + 1) in d:
            if d[(a - 1, b + 1)].buildings != []:
                if d[(a - 1, b + 1)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a - 1, b + 1)].buildings[0])
                    self.buildings.append(c)
                    return c
        if (a + 1 , b - 1) in d:
            if d[(a + 1, b - 1)].buildings != []:
                if d[(a + 1, b - 1)].buildings[0].typ == "village":
                    c = Mine(self.x, self.y, d[(a + 1, b - 1)].buildings[0])
                    self.buildings.append(c)
                    return c
        print("Fuckoff")
               
# Add entities
    def add_soldier(self, owner):
        pass
        
                
        
class Entity(arcade.Sprite):
    def __init__(self, typ,  x, y, health, damage, owner):
        super().__init__("data/entities/" + typ + ".png", center_x = x, center_y = y)
        self.x = x
        self.y = y 
        self.health = health
        self.damage = damage
        self.owner = owner

class Soldier(Entity):
    def __init__(self, x, y, owner):
        super().__init__("soldier", x, y, 10, 3, owner)
        self.x = x
        self.y = y
        self.owner = owner

class Building(arcade.Sprite):
    def __init__(self, x, y, typ):
        super().__init__("data/buildings/" + typ + ".png", center_x = x, center_y = y)
        self.x = x
        self.y = y
        self.typ = typ

class Village(Building):
    def __init__(self, x, y, name, lvl = 1, owner = None):
        super().__init__(x, y, "village")
        self.x = x
        self.y = y
        self.name = name
        self.lvl = lvl
        self.owner = owner

    def levelup(self):
        self.lvl += 1

    def klick(self):
        return sidebar.village(self)

class Mine(Building):
    def __init__(self, x, y, village, lvl = 1):
        super().__init__(x, y, "mine")
        self.x = x
        self.y = y
        self.village = village
        self.owner = village.owner
        self.lvl = lvl
    
    def produce(self):
        self.owner.goods["stone"] += (self.lvl * self.village.lvl)
    
    def klick(self):
        return sidebar.mine(self)


class Player():
    def __init__(self, name, color, tribe, goods: dict = {}):
        self.name = name
        self.color = color
        self.tribe = tribe
        self.goods = goods
        self.startgoods()

    def startgoods(self):
        self.goods["stone"] = 0
        self.goods["wood"] = 0
        self.goods["coal"] = 0
        self.goods["wheat"] = 0
        self.goods["flour"] = 0
        self.goods["iron"] = 0
        self.goods["gold"] = 0
        self.goods["swords"] = 0


sp = Suchspiel(1000, 800, "NATIONWARS", 24, 24)
arcade.run()