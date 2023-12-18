import arcade, random as r, arcade.gui
import reader, sidebar, topbar, tree

# Technologies
t_quarry = False



class Suchspiel(arcade.Window):
    def __init__(self, breite, höhe, titel, feld_h, feld_b):
        super().__init__(breite, höhe, titel)
        arcade.set_background_color((155,155,155)) 
        self.fields = arcade.SpriteList()
        self.buildings = arcade.SpriteList()
        self.entities = arcade.SpriteList()
        self.players = []
        self.turn = 1
        self.sbar = []
        self.sbar = sidebar.start()
        self.tbar = []
        self.overlays = arcade.SpriteList()
        
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
        self.entities.append(Soldier(self.Dictionary[(2,2)], self.players[0]))
        self.buildings.append(self.fields[98].add_village("München", self.players[0])) 
        self.buildings.append(self.fields[99].add_quarry(self.Dictionary, None))
        self.buildings.append(self.fields[387].add_village("Berlin", self.players[0])) 
        self.buildings.append(self.fields[386].add_quarry(self.Dictionary, None)) 
        

        self.tbar = topbar.start(self.players[0])


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(1,1), (0,1), (0,0), (1,0)])
        if button == 1:
            kfields = False
            for i in self.fields:
                if arcade.check_for_collision(pseudosprite, i):
                    kfields = True
                    self.active = i.select(self.Dictionary, self.fields, self.active)
                    self.sbar.clear()
                    a = i.klick(self.Dictionary)
                    for i in a:
                        self.sbar.append(i)
            
            kbuildings = False
            for i in self.buildings:
                if arcade.check_for_collision(pseudosprite, i):
                    kbuildings = True
                    self.sbar.clear()
                    a = i.klick()
                    for i in a:
                        self.sbar.append(i)

            koverlays = False
            for i in self.overlays:
                if arcade.check_for_collision(pseudosprite, i):
                    koverlays = True
                    a = i.klick()

            kentities = False
            self.overlays.clear()
            for i in self.entities:
                if i.used == False:
                    if arcade.check_for_collision(pseudosprite, i):
                        self.time_since_clicked = 0
                        kentities = True
                        self.sbar.clear()
                        tulplehässlichding = i.klick(self.Dictionary, self.overlays)
                        a = tulplehässlichding[0]
                        self.overlays = tulplehässlichding[1]

                        for i in a:
                            self.sbar.append(i)
                    
            kbuttons = False
            for i in self.sbar:
                if i.type == "Button":
                    if arcade.check_for_collision(pseudosprite, i):
                        kbuttons = True
                        if i.f == "add_village":
                            self.buildings.append(self.active.add_village("Hamburg", self.players[0]))
                            self.sbar.clear()
                            self.sbar = sidebar.start()
                        if i.f == "add_quarry":
                            e = self.active.add_quarry(self.Dictionary, self.players[0])
                            self.buildings.append(e)
                            self.sbar.clear()
                            self.sbar = sidebar.quarry(e)
                        if i.f == "upgrade_quarry":
                            for j in self.active.buildings:
                                if j.typ == "quarry":
                                    j.lvl += 1
                                    self.sbar.clear()
                                    self.sbar = sidebar.quarry(j)
                        if i.f == "add_mine":
                            e = self.active.add_mine(self.Dictionary, self.players[0])
                            self.buildings.append(e)
                            self.sbar.clear()
                            self.sbar = sidebar.mine(e)
                        if i.f == "upgrade_mine":
                            for j in self.active.buildings:
                                if j.typ == "mine":
                                    j.lvl += 1
                                    self.sbar.clear()
                                    self.sbar = sidebar.mine(j)
                        if i.f == "add_cabin":
                            e = self.active.add_cabin(self.Dictionary, self.players[0])
                            self.buildings.append(e)
                            self.sbar.clear()
                            self.sbar = sidebar.cabin(e)
                        if i.f == "upgrade_cabin":
                            for j in self.active.buildings:
                                if j.typ == "cabin":
                                    j.lvl += 1
                                    self.sbar.clear()
                                    self.sbar = sidebar.cabin(j)

                        if i.f == "open_investigations":
                            self.sbar.clear()
                            self.sbar = sidebar.investigationstree()

                        if i.f == "open_it_productions":
                            self.sbar.clear()
                            self.sbar = sidebar.open_it_productions(self.players[0])

                        if i.f == "open_t_quarry":
                            if self.players[0].technologies["quarry"] != True:
                                self.sbar.clear()
                                self.sbar = sidebar.open_t_quarry()
                            
                        if i.f == "investigate_quarry":
                            self.sbar.clear()
                            self.players[0].technologies["quarry"] = True
                            self.sbar = sidebar.investigationstree()

                        if i.f == "open_t_cabin":
                            if self.players[0].technologies["cabin"] != True:
                                self.sbar.clear()
                                self.sbar = sidebar.open_t_cabin()
                            
                        if i.f == "investigate_cabin":
                            self.sbar.clear()
                            self.players[0].technologies["cabin"] = True
                            self.sbar = sidebar.investigationstree()

                        if i.f == "open_t_wheat_plot":
                            if self.players[0].technologies["wheat_plot"] != True:
                                self.sbar.clear()
                                self.sbar = sidebar.open_t_wheat_plot()
                            
                        if i.f == "investigate_wheat_plot":
                            self.sbar.clear()
                            self.players[0].technologies["wheat_plot"] = True
                            self.sbar = sidebar.investigationstree()

                        if i.f == "open_t_pasture":
                            if self.players[0].technologies["pasture"] != True:
                                self.sbar.clear()
                                self.sbar = sidebar.open_t_pasture()
                            
                        if i.f == "investigate_pasture":
                            self.sbar.clear()
                            self.players[0].technologies["pasture"] = True
                            self.sbar = sidebar.investigationstree()





                        if i.f == "pass_turn":
                            self.produce()
                            self.tbar = topbar.start(self.players[0])
                            self.turn += 1/len(self.players)
                    
                            for i in self.entities:
                                i.used = False


                        


            if kfields == False and kbuildings == False and kbuttons == False and kentities == False and koverlays == False:
                self.sbar.clear()
                a = sidebar.start()
                for i in a:
                    self.sbar.append(i)


        elif button == 2 or button == 4:
            for i in self.fields:
                if arcade.check_for_collision(pseudosprite, i):
                    pass

    def on_draw(self):
        self.clear()
        self.fields.draw()  
        self.buildings.draw()
        self.overlays.draw()        
        self.entities.draw()
        for i in self.sbar:
            i.draw()
        for i in self.tbar:
            if i.type != "Txt":
                i.draw(pixelated = True)
            else:
                i.draw()
    
    def produce(self):
        for i in self.buildings:
            i.produce()
    

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
    
    def klick(self, d):
        return sidebar.field(self, d, None)

    def add_village(self, name, owner):
        a = Village(self.x, self.y, name, 1, owner)
        self.buildings.append(a) 
        return a
    
    def add_quarry(self, d, owner):
        if self.typ != "mountain":
            raise(TypeError)
        a,b = self.pos_for_village(d, owner)
        c = Quarry(self.x, self.y, d[(a, b)].buildings[0])
        self.buildings.append(c)
        return c
    
    def add_mine(self, d, owner):
        if self.typ != "mountain":
            raise(TypeError)
        a,b = self.pos_for_village(d, owner)
        c = Mine(self.x, self.y, d[(a, b)].buildings[0])
        self.buildings.append(c)
        return c
    
    def add_cabin(self, d, owner):
        if self.typ != "forest":
            raise(TypeError)
        a,b = self.pos_for_village(d, owner)
        c = Cabin(self.x, self.y, d[(a, b)].buildings[0])
        self.buildings.append(c)
        return c
               
# Add entities
    def add_soldier(self, owner):
        pass

    def pos_for_village(self, d, owner):
        a, b = self.pos
        if (a + 1, b) in d:
            if d[(a + 1, b)].buildings != []:
                if d[(a + 1, b)].buildings[0].typ == "village":
                    return (a + 1, b)
        if (a, b + 1) in d:
            if d[(a, b + 1)].buildings != []:
                if d[(a, b + 1)].buildings[0].typ == "village":
                    return (a, b + 1)
        if (a - 1 , b) in d:
            if d[(a - 1, b)].buildings != []:
                if d[(a - 1, b)].buildings[0].typ == "village":
                    return (a - 1, b)
        if (a, b - 1) in d:
            if d[(a, b - 1)].buildings != []:
                if d[(a, b - 1)].buildings[0].typ == "village":
                    return (a, b - 1)
        if (a + 1, b + 1) in d:
            if d[(a + 1, b + 1)].buildings != []:
                if d[(a + 1, b + 1)].buildings[0].typ == "village":
                    return (a + 1, b + 1)
        if (a - 1 , b - 1) in d:
            if d[(a - 1, b - 1)].buildings != []:
                if d[(a - 1, b - 1)].buildings[0].typ == "village":
                    return (a - 1, b - 1)
        if (a - 1, b + 1) in d:
            if d[(a - 1, b + 1)].buildings != []:
                if d[(a - 1, b + 1)].buildings[0].typ == "village":
                    return (a - 1, b + 1)
        if (a + 1 , b - 1) in d:
            if d[(a + 1, b - 1)].buildings != []:
                if d[(a + 1, b - 1)].buildings[0].typ == "village":
                    return (a + 1, b - 1)

# Others   
    def test_for_village(self, d, owner):
        a, b = self.pos
        if (a + 1, b) in d:
            if d[(a + 1, b)].buildings != []:
                if d[(a + 1, b)].buildings[0].typ == "village":
                    return True
        if (a, b + 1) in d:
            if d[(a, b + 1)].buildings != []:
                if d[(a, b + 1)].buildings[0].typ == "village":
                    return True
        if (a - 1 , b) in d:
            if d[(a - 1, b)].buildings != []:
                if d[(a - 1, b)].buildings[0].typ == "village":
                    return True
        if (a, b - 1) in d:
            if d[(a, b - 1)].buildings != []:
                if d[(a, b - 1)].buildings[0].typ == "village":
                    return True
        if (a + 1, b + 1) in d:
            if d[(a + 1, b + 1)].buildings != []:
                if d[(a + 1, b + 1)].buildings[0].typ == "village":
                    return True
        if (a - 1 , b - 1) in d:
            if d[(a - 1, b - 1)].buildings != []:
                if d[(a - 1, b - 1)].buildings[0].typ == "village":
                    return True
        if (a - 1, b + 1) in d:
            if d[(a - 1, b + 1)].buildings != []:
                if d[(a - 1, b + 1)].buildings[0].typ == "village":
                    return True
        if (a + 1 , b - 1) in d:
            if d[(a + 1, b - 1)].buildings != []:
                if d[(a + 1, b - 1)].buildings[0].typ == "village":
                    return True
        return False
            

class Overlay(arcade.Sprite):
    def __init__(self, field, tex, entity):
        super().__init__(tex , center_x = field.x, center_y = field.y)
        self.entity = entity
        self.field = field

    def klick(self):
        self.entity.center_x = self.center_x
        self.entity.center_y = self.center_y
        self.entity.field = self.field
        self.entity.used = True



class Entity(arcade.Sprite):
    def __init__(self, typ, field, health, damage, owner):
        super().__init__("data/entities/" + typ + ".png", center_x = field.x, center_y = field.y)    
        self.field = field
        self.health = health
        self.damage = damage
        self.owner = owner
        self.klicked = False
        self.typ = typ
        self.used = False

    def on_key_press(self, symbol):
        if symbol == arcade.key.UP:
            print("ja")
            self.field.pos = [0,0]

    def klick(self, d, o):
        return (sidebar.entity(self), self.test_for_fields(d, o, None))
    
    def test_for_fields(self, d, overlays, owner):
        a, b = self.field.pos
        if (a + 1, b) in d:
            overlays.append(Overlay(d[a+1, b], "data/icons/overlay.png", self))
            
        if (a, b + 1) in d:
            overlays.append(Overlay(d[a, b+1], "data/icons/overlay.png", self))
            
        if (a - 1 , b) in d:
            overlays.append(Overlay(d[a-1, b], "data/icons/overlay.png", self))

        if (a, b - 1) in d:
            overlays.append(Overlay(d[a, b-1], "data/icons/overlay.png", self))

        if (a + 1, b + 1) in d:  
            overlays.append(Overlay(d[a+1, b+1], "data/icons/overlay.png", self))

        if (a - 1 , b - 1) in d:
            overlays.append(Overlay(d[a-1, b-1], "data/icons/overlay.png", self))

        if (a - 1, b + 1) in d:
            overlays.append(Overlay(d[a-1, b+1], "data/icons/overlay.png", self))

        if (a + 1 , b - 1) in d:
            overlays.append(Overlay(d[a+1, b-1], "data/icons/overlay.png", self))

        return overlays  

        
    def check_for_field(self):
        x = self.field.x
        y = self.field.y
  

class Soldier(Entity):
    def __init__(self, field, owner):
        super().__init__("Soldier", field, 10, 3, owner )
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

    def klick(self):
        return sidebar.village(self)
    
    def produce(self):
        self.owner.coins += r.randint(2, 10) * self.lvl

class Quarry(Building):
    def __init__(self, x, y, village, lvl = 1):
        super().__init__(x, y, "quarry")
        self.x = x
        self.y = y
        self.village = village
        self.owner = village.owner
        self.lvl = lvl
    
    def produce(self):
        self.owner.goods["stone"] += (self.lvl * self.village.lvl)
    
    def klick(self):
        return sidebar.quarry(self)

class Mine(Building):
    def __init__(self, x, y, village, lvl = 1):
        super().__init__(x, y, "mine")
        self.x = x
        self.y = y
        self.village = village
        self.owner = village.owner
        self.lvl = lvl
    
    def produce(self):
        self.owner.goods["iron"] += (self.lvl * self.village.lvl)
    
    def klick(self):
        return sidebar.mine(self)


class Cabin(Building):
    def __init__(self, x, y, village, lvl = 1):
        super().__init__(x, y, "cabin")
        self.x = x
        self.y = y
        self.village = village
        self.owner = village.owner
        self.lvl = lvl
    
    def produce(self):
        self.owner.goods["wood"] += (self.lvl * self.village.lvl)
    
    def klick(self):
        return sidebar.cabin(self)

class Player():
    def __init__(self, name, color, tribe, goods: dict = {}, technologies: dict = {}):
        self.name = name
        self.color = color
        self.tribe = tribe
        self.coins = 0
        self.investigationpoints = 0
        self.goods = goods
        self.technologies = technologies
        self.startgoods()
        self.startt()

    def startgoods(self):
        self.goods["stone"] = 0
        self.goods["wood"] = 0
        self.goods["coal"] = 0
        self.goods["wheat"] = 0
        self.goods["flour"] = 0
        self.goods["iron"] = 0
        self.goods["gold"] = 0
        self.goods["swords"] = 0
        self.goods["bows"] = 0

    def startt(self):
        self.technologies["quarry"] = False
        self.technologies["cabin"] = False
        self.technologies["wheat_plot"] = False
        self.technologies["pasture"] = False
        # self.technologies["quarry"] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False
        # self.technologies[] = False








#klassen

class Button(arcade.Sprite):
    def __init__(self, f, h):
        super().__init__("data/buttons/" + f + ".png", center_x = 890, center_y = h*84 - 10)
        self.f = f 
        self.type = "Button"

class Txt(arcade.Text):
    def __init__(self, txt, x, y, color, b = False):
        super().__init__(txt, x, y, color, font_name="data/fonts/minimalistic.ttf", font_size = 16, bold = b)
        self.type = "Txt"

class Img(arcade.Sprite):
    def __init__(self, file, x, y):
        super().__init__(file, scale= 2, center_x = x, center_y = y)
        self.type = "Img"

sp = Suchspiel(1000, 840, "NATIONWARS", 24, 24)
arcade.run() 