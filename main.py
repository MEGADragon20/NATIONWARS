import arcade, random as r, arcade.gui
import reader, sidebar, topbar
from math import ceil
import random
from instances import Instances


class Suchspiel(arcade.Window):
    def __init__(self, breite, höhe, titel, feld_h, feld_b):
        Instances.game = self
        super().__init__(breite, höhe, titel)
        arcade.set_background_color((155,155,155))
        self.activefield = 0
        self.fields = arcade.SpriteList()
        self.buildings = arcade.SpriteList()
        self.entities = arcade.SpriteList()
        self.players = []
        self.turn = 1
        self.sbar = []
        self.players.append(Player("Markus Söder", arcade.color.BLIZZARD_BLUE, "Conquerus"))
        self.players.append(Player("Olaf Scholz", arcade.color.RED_DEVIL, "Uruks"))
        self.sbar = sidebar.start(self.players[0])
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
        self.active_selector = arcade.Sprite("data/icons/active.png", center_x= -16, center_y= -16)
        self.buildings.append(self.fields[98].add_village("München", self.players[0], invisible = True))
        self.buildings.append(self.fields[387].add_village("Berlin", self.players[1], invisible = True))



        self.tbar = topbar.start(self.players[0])

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.ENTER:
            #give him his new stuff haha
            self.produce()
            # change active player
            b = self.players[0]
            self.players.pop(0)
            self.players.append(b)
            # give next player his tbar
            self.tbar = topbar.start(self.players[0])
            self.sbar = sidebar.start(self.players[0])
            # add 1 to the turn-counters (which actually counts every player as a turn => actual turns int(self.truns/len(players)))
            self.turn += 1
            # if the amount of turns to be allowed to build a village is not allready 0, decrease it by one
            if self.players[0].turnstovillage:
                self.players[0].turnstovillage -= 1
            for i in self.entities:
                i.used = False

    def on_key_release(self, symbol, modifiers):
        w = 24 # width of the field
        h = 24 # height of the field
        def setactivefield(activefield):
            i = self.fields[activefield]
            self.active_selector = i.select(self.active_selector)
            self.active = i
            self.sbar.clear()
            a = i.klick(self.Dictionary, self.players[0])
            for i in a:
                self.sbar.append(i)

        if symbol == arcade.key.MOTION_LEFT:
            if self.activefield % w == 0:
                self.activefield += (w + w-1)
            else:
                self.activefield -= 1
            if self.activefield < 0:
                self.activefield = 0
            elif self.activefield > len(self.fields)-1:
                self.activefield = (len(self.fields)-1 - (w-1))
            setactivefield(self.activefield)
        elif symbol == arcade.key.MOTION_RIGHT:
            if self.activefield % w == w-1:
                self.activefield -= (w + w-1)
            else: 
                self.activefield += 1
            if self.activefield > len(self.fields)-1:
                self.activefield = len(self.fields)-1
            elif self.activefield < 0:
                self.activefield = (w-1)
            setactivefield(self.activefield)
        elif symbol == arcade.key.MOTION_UP:
            if self.activefield + w > len(self.fields)-1:
                self.activefield -= w*(h-1)
            else:
                self.activefield += w
            setactivefield(self.activefield)
        elif symbol == arcade.key.MOTION_DOWN:
            if self.activefield - w < 0:
                self.activefield += w*(h-1)
            else:
                self.activefield -= w
            setactivefield(self.activefield)
        
        # other direction 1:
            # elif symbol == arcade.key.MOTION_UP:
            #     print(self.activefield)
            #     if self.activefield + w > len(self.fields)-1:
            #         # self.activefield = (len(self.fields)-1 - (w-1))
            #         if self.activefield == w*h -1:
            #             self.activefield = 0
            #         else:
            #             self.activefield -= w*(h-1) -1
            #     else:
            #         self.activefield += w
            #     setactivefield(self.activefield)
            # elif symbol == arcade.key.MOTION_DOWN:
            #     print(self.activefield)
            #     if self.activefield - w < 0:
            #         # self.activefield += (w-1)
            #         if self.activefield == 0:
            #             self.activefield = w*h -1
            #         else:
            #             self.activefield += w*(h-1) -1
            #     else:
            #         self.activefield -= w
            #     setactivefield(self.activefield)
        # other direction 2:
            # elif symbol == arcade.key.MOTION_UP:
            #     print(self.activefield)
            #     if self.activefield + w > len(self.fields)-1:
            #         # self.activefield = (len(self.fields)-1 - (w-1))
            #         if self.activefield == w*(h-1):
            #             self.activefield = (w-1)
            #         else:
            #             self.activefield -= 1 + w*(h-1)
            #     else:
            #         self.activefield += w
            #     setactivefield(self.activefield)
            # elif symbol == arcade.key.MOTION_DOWN:
            #     print(self.activefield)
            #     if self.activefield - w < 0:
            #         # self.activefield += (w-1)
            #         if self.activefield == (w-1):
            #             self.activefield = w*(h-1)
            #         else:
            #             self.activefield += 1 + w*(h-1)
            #     else:
            #         self.activefield -= w
            #     setactivefield(self.activefield)

        if self.sbar:
            new = list(filter(lambda x: x.type == "Button", self.sbar))
            if symbol == arcade.key.KEY_0:
                print("0")
                i = new[0]
            elif symbol == arcade.key.KEY_1:
                print("1")
                i = new[1]
            elif symbol == arcade.key.KEY_2:
                print("2")
                i = new[2]
            elif symbol == arcade.key.KEY_3:
                print("3")
                i = new[3]
            elif symbol == arcade.key.KEY_4:
                print("4")
                i = new[4]
            elif symbol == arcade.key.KEY_5:
                print("5")
                i = new[5]
            elif symbol == arcade.key.KEY_6:
                print("6")
                i = new[6]
            elif symbol == arcade.key.KEY_7:
                print("7")
                i = new[7]
            elif symbol == arcade.key.KEY_8:
                print("8")
                i = new[8]
            elif symbol == arcade.key.KEY_9:
                print("9")
                i = new[9]

            try:
                if i.f == "add_village":
                    self.buildings.append(self.active.add_village("Hamburg", self.players[0]))
                    self.sbar.clear()
                    self.sbar = sidebar.start(self.players[0])


                elif i.f == "add_quarry":
                    self.add_building("quarry")
                elif i.f == "add_cabin":
                    self.add_building("cabin")
                elif i.f == "add_wheat_plot":
                    self.add_building("wheat_plot")
                elif i.f == "add_pasture":
                    self.add_building("pasture")
                elif i.f == "add_mine":
                    self.add_building("mine")

                # upgrade building
                elif i.f == "upgrade_quarry":
                    self.upgrade_building("quarry")
                elif i.f == "upgrade_cabin":
                    self.upgrade_building("cabin")
                elif i.f == "upgrade_wheat_plot":
                    self.upgrade_building("wheat_plot")
                elif i.f == "upgrade_pasture":
                    self.upgrade_building("pasture")
                elif i.f == "upgrade_mine":
                    self.upgrade_building("mine")

                # open technology sb
                elif i.f == "open_t_quarry":
                    self.open_technology("quarry")
                elif i.f == "open_t_cabin":
                    self.open_technology("cabin")
                elif i.f == "open_t_wheat_plot":
                    self.open_technology("wheat_plot")
                elif i.f == "open_t_pasture":
                    self.open_technology("pasture")
                elif i.f == "open_t_mine":
                    self.open_technology("mine")

                # investigate
                elif i.f == "investigate_quarry":
                    self.investigate_technology("quarry")
                elif i.f == "investigate_cabin":
                    self.investigate_technology("cabin")
                elif i.f == "investigate_wheat_plot":
                    self.investigate_technology("wheat_plot")
                elif i.f == "investigate_pasture":
                    self.investigate_technology("pasture")
                elif i.f == "investigate_mine":
                    self.investigate_technology("mine")

                elif i.f == "open_investigations":
                    self.sbar.clear()
                    self.sbar = sidebar.investigationstree()

                elif i.f == "open_it_productions":
                    self.sbar.clear()
                    self.sbar = sidebar.open_it_productions(self.players[0])


                # army stuff
                elif i.f == "recruit":
                    if self.players[0] == self.active.buildings[0].owner:
                        self.sbar = sidebar.entities()

                elif i.f == "recruit_soldier":
                    sol = Soldier(self.active, self.players[0])
                    self.entities.append(sol)
                    self.active.entities.append(sol)

                elif i.f == "recruit_recon":
                    rec = Recon(self.active, self.players[0])
                    self.entities.append(rec)
                    self.active.entities.append(rec)


                #default stuff
                elif i.f == "home":
                    self.sbar = sidebar.start(self.players[0])

                elif i.f == "pass_turn":
                    if self.players[0].turnstovillage:
                        self.players[0].turnstovillage -= 1
                    self.turn += 1
                    #give him his new stuff haha
                    self.produce()
                    # change active player
                    b = self.players[0]
                    self.players.pop(0)
                    self.players.append(b)
                    # give next player his tbar
                    self.tbar = topbar.start(self.players[0])
                    self.sbar = sidebar.start(self.players[0])
                    #

                    for i in self.entities:
                        i.used = False
                    for i in self.buildings:
                        if i.typ == "village":
                            i.used = False
            except UnboundLocalError:
                pass



    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(1,1), (0,1), (0,0), (1,0)])
        if button == 1:
            for i in self.fields:
                if arcade.check_for_collision(pseudosprite, i):
                    self.active_selector = i.select(self.active_selector)
                    self.active = i
                    self.sbar.clear()
                    a = i.klick(self.Dictionary, self.players[0])
                    for j in a:
                        self.sbar.append(j)
                    
                    self.activefield = self.fields.index(i)

            for i in self.buildings:
                if arcade.check_for_collision(pseudosprite, i):
                    self.sbar.clear()
                    a = i.klick(self.players[0])
                    for i in a:
                        self.sbar.append(i)

            for i in self.overlays:
                if arcade.check_for_collision(pseudosprite, i):
                    a = i.klick(self.Dictionary)
                    if a == True:
                        self.entities.pop(0)


            self.overlays.clear()
            for i in self.entities:
                if arcade.check_for_collision(pseudosprite, i):
                    self.sbar.clear()
                    tulplehässlichding = i.klick(self.Dictionary, self.overlays, self.players[0])
                    a = tulplehässlichding[0]
                    self.overlays = tulplehässlichding[1]
                    for i in a:
                        self.sbar.append(i)

            for i in self.sbar:
                if i.type == "Button":
                    if arcade.check_for_collision(pseudosprite, i):

                        # FUNCTIONS FOR BUTTONS

                        # add buildings
                        if i.f == "add_village":
                            self.buildings.append(self.active.add_village("Hamburg", self.players[0]))
                            self.sbar.clear()
                            self.sbar = sidebar.start(self.players[0])


                        elif i.f == "add_quarry":
                            self.add_building("quarry")
                        elif i.f == "add_cabin":
                            self.add_building("cabin")
                        elif i.f == "add_wheat_plot":
                            self.add_building("wheat_plot")
                        elif i.f == "add_pasture":
                            self.add_building("pasture")
                        elif i.f == "add_mine":
                            self.add_building("mine")

                        elif i.f == "takeover":
                            newplayer = self.players[0]
                            for building in self.buildings:
                                if isinstance(building, Village) and arcade.check_for_collision(building, self.fields[self.activefield]):
                                    building.owner = newplayer


                        # upgrade building
                        elif i.f == "upgrade_quarry":
                            self.upgrade_building("quarry")
                        elif i.f == "upgrade_cabin":
                            self.upgrade_building("cabin")
                        elif i.f == "upgrade_wheat_plot":
                            self.upgrade_building("wheat_plot")
                        elif i.f == "upgrade_pasture":
                            self.upgrade_building("pasture")
                        elif i.f == "upgrade_mine":
                            self.upgrade_building("mine")

                        # open technology sb
                        elif i.f == "open_t_quarry":
                            self.open_technology("quarry")
                        elif i.f == "open_t_cabin":
                            self.open_technology("cabin")
                        elif i.f == "open_t_wheat_plot":
                            self.open_technology("wheat_plot")
                        elif i.f == "open_t_pasture":
                            self.open_technology("pasture")
                        elif i.f == "open_t_mine":
                            self.open_technology("mine")

                        # investigate
                        elif i.f == "investigate_quarry":
                            self.investigate_technology("quarry")
                        elif i.f == "investigate_cabin":
                            self.investigate_technology("cabin")
                        elif i.f == "investigate_wheat_plot":
                            self.investigate_technology("wheat_plot")
                        elif i.f == "investigate_pasture":
                            self.investigate_technology("pasture")
                        elif i.f == "investigate_mine":
                            self.investigate_technology("mine")

                        elif i.f == "open_investigations":
                            self.sbar.clear()
                            self.sbar = sidebar.investigationstree()

                        elif i.f == "open_it_productions":
                            self.sbar.clear()
                            self.sbar = sidebar.open_it_productions(self.players[0])


                        # army stuff
                        elif i.f == "recruit":
                            if self.players[0] == self.active.buildings[0].owner:
                                self.sbar = sidebar.entities()

                        elif i.f == "recruit_soldier":
                            sol = Soldier(self.active, self.players[0])
                            self.entities.append(sol)
                            self.active.entities.append(sol)

                        elif i.f == "recruit_recon":
                            rec = Recon(self.active, self.players[0])
                            self.entities.append(rec)
                            self.active.entities.append(rec)


                        #default stuff
                        elif i.f == "home":
                            self.sbar = sidebar.start(self.players[0])

                        elif i.f == "pass_turn":
                            if self.players[0].turnstovillage:
                                self.players[0].turnstovillage -= 1
                            self.turn += 1
                            #give him his new stuff haha
                            self.produce()
                            # change active player
                            b = self.players[0]
                            self.players.pop(0)
                            self.players.append(b)
                            # give next player his tbar
                            self.tbar = topbar.start(self.players[0])
                            self.sbar = sidebar.start(self.players[0])
                            #

                            for i in self.entities:
                                i.used = False
                            for i in self.buildings:
                                if i.typ == "village":
                                    i.used = False


        elif button == 2 or button == 4:
            for i in self.fields:
                if arcade.check_for_collision(pseudosprite, i):
                    pass


    def on_draw(self):
        self.clear()
        self.fields.draw()
        self.buildings.draw()
        self.entities.draw()
        self.active_selector.draw()
        self.overlays.draw()

        # show amount of rounds
        # an extra "." if the first person is playing
        arcade.draw_text(str(ceil((self.turn)/len(self.players))),
                         SCREENWIDTH-2*24,
                         SCREENHEIGHT-2*24,
                         arcade.color.BLACK,
                         12 * 2)

        for i in self.sbar:
            i.draw()
        for i in self.tbar:
            if i.type != "Txt":
                i.draw(pixelated = True)
            else:
                i.draw()

    def produce(self):
        for i in self.buildings:
            if i.owner.name == self.players[0].name:
                i.produce()

    def open_technology(self, tech_type):
        if not self.players[0].technologies.get(tech_type, False):
            self.sbar.clear()
            self.sbar = getattr(sidebar, f"open_t_{tech_type}")()

    def investigate_technology(self, tech_type):
        if self.players[0].investigationpoints >= 1:
            self.players[0].investigationpoints -= 1
            self.tbar = topbar.start(self.players[0])
            self.sbar.clear()
            self.players[0].technologies[tech_type] = True
            self.sbar = sidebar.investigationstree()
        else:
            raise ValueError

    def add_building(self, building_type):
        if self.players[0].coins >= 25:
            self.players[0].coins -= 25
            self.tbar = topbar.start(self.players[0])
            building_instance = getattr(self.active, f"add_{building_type}")(self.Dictionary, self.players[0])
            self.buildings.append(building_instance)
            self.sbar.clear()
            self.sbar = getattr(sidebar, building_type)(building_instance)
        else:
            raise ValueError

    def upgrade_building(self, building_type):

        for building in self.active.buildings:
            if building.typ == building_type:
                costtype1 = None
                costtype2 = None
                faktor = 1

                # Auswählen der kosten

                if building_type == "quarry":
                    costtype1 = "stone"
                    costtype2 = "wood"
                elif building_type == "cabin":
                    costtype1 = "wood"
                    costtype2 = "wool"
                elif building_type == "pasture":
                    costtype1 = "wool"
                    costtype2 = "wheat"
                elif building_type == "wheat_plot":
                    costtype1 = "wheat"
                    costtype2 = "iron"
                elif building_type == "mine":
                    costtype1 = "iron"
                    costtype2 = "stone"
                faktor = round(building.lvl/2 + 0.1) # Aufrunden

                if self.players[0].goods[costtype1] >= 5*faktor and self.players[0].goods[costtype2] >= 2*faktor:
                    self.players[0].goods[costtype1] -= 5*faktor
                    self.players[0].goods[costtype2] -= 2*faktor
                    self.tbar = topbar.start(self.players[0])



                    building.lvl += 1
                    self.sbar.clear()
                    self.sbar = getattr(sidebar, building_type)(building)
                else:
                    raise ValueError

class Field(arcade.Sprite):
    def __init__(self,  x, y, typ):
        super().__init__("data/fields/" + typ + ".png", center_x = x, center_y = y)
        self.x = x
        self.y = y
        self.typ = typ
        self.pos = (((self.x - 32)/32),((self.y - 32)/ 32))
        self.buildings = []
        self.entities = []

    def select(self, active):
        active.center_x = self.center_x
        active.center_y = self.center_y
        return active

    def klick(self, d, player):
        return sidebar.field(self, d, player)

    # invisible determines if the village should reset the counter for the next village-build (True at the beginning, when the game is being initialized)
    def add_village(self, name, owner, invisible=False):
        # reset counter (until village-build is allowed)
        a = Village(self.x, self.y, name, 1, owner)
        if not invisible:
            owner.turnstovillage = 10
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

    def add_wheat_plot(self, d, owner):
        if self.typ != "grass":
            raise(TypeError)
        a,b = self.pos_for_village(d, owner)
        c = Wheat_plot(self.x, self.y, d[(a, b)].buildings[0])
        self.buildings.append(c)
        return c

    def add_pasture(self, d, owner):
        if self.typ != "grass":
            raise(TypeError)
        a,b = self.pos_for_village(d, owner)
        c = Pasture(self.x, self.y, d[(a, b)].buildings[0])
        self.buildings.append(c)
        return c


# Add entities
    def add_soldier(self, owner):
        pass

    def neighbor_for_village(self, d, owner): #!!! owner is not used
        a, b = self.pos


        print(d)
        if (a + 1, b) in d:
            if d[(a + 1, b)].buildings != []:
                if d[(a + 1, b)].buildings[0].typ == "village":

                    return d[(a + 1, b)].buildings[0]
        if (a, b + 1) in d:
            if d[(a, b + 1)].buildings != []:
                if d[(a, b + 1)].buildings[0].typ == "village":

                    return d[(a, b + 1)].buildings[0]
        if (a - 1 , b) in d:
            if d[(a - 1, b)].buildings != []:
                if d[(a - 1, b)].buildings[0].typ == "village":

                    return d[(a - 1, b)].buildings[0]
        if (a, b - 1) in d:
            if d[(a, b - 1)].buildings != []:
                if d[(a, b - 1)].buildings[0].typ == "village":

                    return d[(a, b - 1)].buildings[0]
        if (a + 1, b + 1) in d:
            if d[(a + 1, b + 1)].buildings != []:
                if d[(a + 1, b + 1)].buildings[0].typ == "village":

                    return d[(a + 1, b + 1)].buildings[0]
        if (a - 1 , b - 1) in d:
            if d[(a - 1, b - 1)].buildings != []:
                if d[(a - 1, b - 1)].buildings[0].typ == "village":

                    return d[(a - 1, b - 1)].buildings[0]
        if (a - 1, b + 1) in d:
            if d[(a - 1, b + 1)].buildings != []:
                if d[(a - 1, b + 1)].buildings[0].typ == "village":

                    return d[(a - 1, b + 1)].buildings[0]
        if (a + 1 , b - 1) in d:
            if d[(a + 1, b - 1)].buildings != []:
                if d[(a + 1, b - 1)].buildings[0].typ == "village":

                    return d[(a + 1, b - 1)].buildings[0]

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
    def klick(self, d):
        kill = False
        if self.field.entities != []:
            self.field.entities[0].health -= self.entity.damage
            if self.field.entities[0].health <= 0:
                kill = True
                self.field.entities.clear
                self.entity.center_x = self.center_x
                self.entity.center_y = self.center_y
                self.entity.field.entities.clear()
                self.field.entities.append(self.entity)
                self.entity.field = self.field

        else:
            self.entity.center_x = self.center_x
            self.entity.center_y = self.center_y
            self.entity.field.entities.clear()
            self.field.entities.append(self.entity)
            self.entity.field = self.field

        self.entity.used = True
        return kill






class Entity(arcade.Sprite):
    def __init__(self, typ, field, health, damage, owner, feldtyp):
        super().__init__("data/entities/" + typ + ".png", scale = 0.5, center_x = field.x, center_y = field.y)
        self.field = field
        self.health = health
        self.damage = damage
        self.owner = owner
        self.klicked = False
        self.typ = typ
        self.used = False
        self.feldtyp = feldtyp

    def on_key_press(self, symbol):
        if symbol == arcade.key.UP:
            self.field.pos = [0,0]

    def klick(self, d, o, player):
        if self.used == False:
            return (sidebar.entity(self, Village), self.test_for_fields(d, o, None, player))
        else:
            return (sidebar.entity(self, Village), arcade.SpriteList())
    def test_for_fields(self, d, overlays, owner, playeronturn):
        a, b = self.field.pos
        if self.typ == "Soldier" or self.typ == "Recon" or self.typ == "Ship":
                if (a + 1, b) in d:
                    if self.owner == playeronturn:
                        if d[a + 1, b].typ in self.feldtyp:
                            if d[a + 1, b].entities != [] and d[a + 1, b].entities[0].owner != self.owner:
                                overlays.append(Overlay(d[a+1, b], "data/icons/overlayred.png", self))
                            elif d[a + 1, b].entities != [] and d[a + 1, b].entities[0].owner == self.owner:
                                pass
                            else:
                                overlays.append(Overlay(d[a+1, b], "data/icons/overlay.png", self))
                if (a, b + 1) in d:
                    if self.owner == playeronturn:
                            if d[a , b+1].typ in self.feldtyp:
                                if d[a , b+1].entities != [] and d[a, b + 1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a, b + 1], "data/icons/overlayred.png", self))
                                elif d[a , b+1].entities != [] and d[a, b + 1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a, b + 1], "data/icons/overlay.png", self))
                if (a - 1 , b) in d:
                    if self.owner == playeronturn:
                            if d[a - 1, b].typ in self.feldtyp:
                                if d[a - 1, b].entities != [] and d[a - 1, b].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a - 1 , b], "data/icons/overlayred.png", self))
                                elif d[a - 1, b].entities != [] and d[a - 1, b].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a - 1 , b], "data/icons/overlay.png", self))
                if (a, b - 1) in d:
                    if self.owner == playeronturn:
                        if d[a , b - 1].typ in self.feldtyp:
                            if d[a , b-1].entities != [] and d[a, b - 1].entities[0].owner != self.owner:
                                overlays.append(Overlay(d[a, b - 1], "data/icons/overlayred.png", self))
                            elif d[a , b-1].entities != [] and d[a, b - 1].entities[0].owner == self.owner:
                                pass
                            else:
                                overlays.append(Overlay(d[a, b - 1], "data/icons/overlay.png", self))
                if (a + 1, b + 1) in d:
                    if self.owner == playeronturn:
                            if d[a + 1 , b + 1].typ in self.feldtyp:
                                if d[a + 1 , b + 1].entities != [] and d[a + 1, b + 1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a + 1, b + 1], "data/icons/overlayred.png", self))
                                elif d[a + 1 , b + 1].entities != [] and d[a + 1, b + 1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a + 1, b + 1], "data/icons/overlay.png", self))
                if (a - 1 , b - 1) in d:
                    if self.owner == playeronturn:
                            if d[a - 1 , b - 1].typ in self.feldtyp:
                                if d[a - 1 , b - 1].entities != [] and d[a - 1, b - 1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a - 1 , b - 1], "data/icons/overlayred.png", self))
                                elif d[a - 1 , b - 1].entities != [] and d[a - 1, b - 1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a - 1 , b - 1], "data/icons/overlay.png", self))
                if (a - 1, b + 1) in d:
                    if self.owner == playeronturn:
                            if d[a - 1 , b + 1].typ in self.feldtyp:
                                if d[a - 1 , b + 1].entities != [] and d[a - 1, b + 1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a - 1, b + 1], "data/icons/overlayred.png", self))
                                elif d[a - 1 , b + 1].entities != [] and d[a - 1, b + 1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a - 1, b + 1], "data/icons/overlay.png", self))
                if (a + 1 , b - 1) in d:
                    if self.owner == playeronturn:
                            if d[a + 1 , b - 1].typ in self.feldtyp:
                                if d[a + 1 , b - 1].entities != [] and d[a + 1, b - 1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a + 1, b-1], "data/icons/overlayred.png", self))
                                elif d[a + 1, b - 1].entities!= [] and d[a + 1, b - 1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a + 1, b-1], "data/icons/overlay.png", self))
        if self.typ == "Recon":
                if (a-1, b-2) in d:
                    if self.owner == playeronturn:
                        if d[a-1, b-2].typ in self.feldtyp:
                            if d[a-1, b-2].entities != [] and d[a-1, b-2].entities[0].owner != self.owner:
                                overlays.append(Overlay(d[a+1, b], "data/icons/overlayred.png", self))
                            elif d[a-1, b-2].entities != [] and d[a-1, b-2].entities[0].owner == self.owner:
                                pass
                            else:
                                overlays.append(Overlay(d[a+1, b], "data/icons/overlay.png", self))
                if (a, b-2) in d:
                    if self.owner == playeronturn:
                            if d[a,b-2].typ in self.feldtyp:
                                if d[a,b-2].entities != [] and d[a,b-2].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a,b-2], "data/icons/overlayred.png", self))
                                elif d[a,b-2].entities != [] and d[a,b-2].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a,b-2], "data/icons/overlay.png", self))
                if (a+1, b-2) in d:
                    if self.owner == playeronturn:
                            if d[a+1,b-2].typ in self.feldtyp:
                                if d[a+1,b-2].entities != [] and d[a+1,b-2].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a+1,b-2], "data/icons/overlayred.png", self))
                                elif d[a+1,b-2].entities != [] and d[a+1,b-2].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a+1,b-2], "data/icons/overlay.png", self))
                if (a-2, b-1) in d:
                    if self.owner == playeronturn:
                            if d[a-2,b-1].typ in self.feldtyp:
                                if d[a-2,b-1].entities != [] and d[a-2,b-1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a-2,b-1], "data/icons/overlayred.png", self))
                                elif d[a-2,b-1].entities != [] and d[a-2,b-1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a-2,b-1], "data/icons/overlay.png", self))
                if (a-2, b) in d:
                    if self.owner == playeronturn:
                            if d[a-2,b].typ in self.feldtyp:
                                if d[a-2,b].entities != [] and d[a-2,b].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a-2,b], "data/icons/overlayred.png", self))
                                elif d[a-2,b].entities != [] and d[a-2,b].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a-2,b], "data/icons/overlay.png", self))
                if (a-2, b+1) in d:
                    if self.owner == playeronturn:
                            if d[a-2,b+1].typ in self.feldtyp:
                                if d[a-2,b+1].entities != [] and d[a-2,b+1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a-2,b+1], "data/icons/overlayred.png", self))
                                elif d[a-2,b+1].entities != [] and d[a-2,b+1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a-2,b+1], "data/icons/overlay.png", self))
                if (a-1, b+2) in d:
                    if self.owner == playeronturn:
                            if d[a-1,b+2].typ in self.feldtyp:
                                if d[a-1,b+2].entities != [] and d[a-1,b+2].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a-1,b+2], "data/icons/overlayred.png", self))
                                elif d[a-1,b+2].entities != [] and d[a-1,b+2].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a-1,b+2], "data/icons/overlay.png", self))
                if (a, b+2) in d:
                    if self.owner == playeronturn:
                            if d[a,b+2].typ in self.feldtyp:
                                if d[a,b+2].entities != [] and d[a,b+2].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a,b+2], "data/icons/overlayred.png", self))
                                elif d[a,b+2].entities != [] and d[a,b+2].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a,b+2], "data/icons/overlay.png", self))
                if (a+1, b+2) in d:
                    if self.owner == playeronturn:
                            if d[a+1,b+2].typ in self.feldtyp:
                                if d[a+1,b+2].entities != [] and d[a+1,b+2].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a+1,b+2], "data/icons/overlayred.png", self))
                                elif d[a+1,b+2].entities != [] and d[a+1,b+2].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a+1,b+2], "data/icons/overlay.png", self))
                if (a+2, b-1) in d:
                    if self.owner == playeronturn:
                            if d[a+2,b-1].typ in self.feldtyp:
                                if d[a+2,b-1].entities != [] and d[a+2,b-1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a+2,b-1], "data/icons/overlayred.png", self))
                                elif d[a+2,b-1].entities != [] and d[a+2,b-1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a+2,b-1], "data/icons/overlay.png", self))
                if (a+2, b) in d:
                    if self.owner == playeronturn:
                            if d[a+2,b].typ in self.feldtyp:
                                if d[a+2,b].entities != [] and d[a+2,b].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a+2,b], "data/icons/overlayred.png", self))
                                elif d[a+2,b].entities != [] and d[a+2,b].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a+2,b], "data/icons/overlay.png", self))
                if (a+2, b+1) in d:
                    if self.owner == playeronturn:
                            if d[a+2,b+1].typ in self.feldtyp:
                                if d[a+2,b+1].entities != [] and d[a+2,b+1].entities[0].owner != self.owner:
                                    overlays.append(Overlay(d[a+2,b+1], "data/icons/overlayred.png", self))
                                elif d[a+2,b+1].entities != [] and d[a+2,b+1].entities[0].owner == self.owner:
                                    pass
                                else:
                                    overlays.append(Overlay(d[a+2,b+1], "data/icons/overlay.png", self))
        return overlays




    def check_for_field(self):
        x = self.field.x
        y = self.field.y


class Soldier(Entity):
    def __init__(self, field, owner):
        super().__init__("Soldier", field, 10, 4, owner, ["grass", "forest", "mountain"])
        self.owner = owner


class Bow(Entity):
    def __init__(self, field, owner):
        super().__init__("Bow", field, 10, 4, owner, ["grass", "forest"])
        self.owner = owner


class Ship(Entity):
    def __init__(self, field, owner):
        super().__init__("Ship", field, 10, 4, owner, ["water"])
        self.owner = owner

class Recon(Entity):
    def __init__(self, field, owner):
        super().__init__("Recon", field, 8, 2, owner, ["grass", "forest"])
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
        self.used = True

    def takeover(self, player):
        if random.randint(0, 2) == 0:
            self.owner = player

    def klick(self, player):
        return sidebar.village(self, player)

    def produce(self):
        self.owner.coins += r.randint(2, 10) * self.lvl
        self.owner.investigationpoints += 1


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

    def klick(self, player):
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

    def klick(self, player):
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

    def klick(self, player):
        return sidebar.cabin(self)


class Wheat_plot(Building):
    def __init__(self, x:any, y:any, village:Village, lvl:int = 1):
        super().__init__(x, y, "wheat_plot")
        self.x:any = x                      # x-coordinate of the wheat plot
        self.y:any = y                      # y-coordinate of the wheat plot
        self.village:Village = village      # the village the wheat plot is part of/belongs to
        self.owner:Player = village.owner   # the owner of the wheat plot
        self.lvl:int = lvl                  # the level of the wheat plot

    def produce(self):
        # wheat plot produces wheat (amount: multiplication of the level of the village and the level of the wheat plot)
        self.owner.goods["wheat"] += (self.lvl * self.village.lvl)

    def klick(self, player):
        # when klicked on, the sidebar for the wheat plot is returned (to e.g. upgrade the wheat plot)
        return sidebar.wheat_plot(self)

class Player():
    DEFAULT:dict[any] = {    # every Player's default values
        "coins": 0,
        "investigationpoints": 0,
        "goods": {
            "stone":  0,
            "wood":   0,
            "wool":   0,
            "wheat":  0,
            "flour":  0,
            "iron":   0,
            "gold":   0,
            "swords": 0,
            "bows":   0
        },
        "technologies": {
            "quarry": False,
            "cabin": False,
            "wheat_plot": False,
            "pasture": False,
            "mine": False
        },
        "turnstovillage": 0
    }

    # the constructor sets the values and attributes of the player
    # the constructor takes a name, color and tribe as arguments, optionally coins, investigationpoints, goods, technologies and turnstovillage, which are set to the default values if not given
    def __init__(self, name:str, color:any, tribe:any, coins:int = DEFAULT["coins"], investigationpoints:int = DEFAULT["investigationpoints"], goods:dict[str, int] = DEFAULT["goods"], technologies:dict[str, int] = DEFAULT["technologies"], turnstovillage:int = DEFAULT["turnstovillage"]):
        self.name:str =                    name                 # the name of the player
        self.color:any =                   color                # the color of the player
        self.tribe:any =                   tribe                # the tribe of which it is a part of

        self.coins:int =                   coins                                            # amount of coins currently owned
        self.investigationpoints:int =     investigationpoints                              # amount of investigationpoints currently owned
        self.turnstovillage:int =          turnstovillage                                   # turns left untill a village can be built (intervall of 10)
        # the dictionaries are being combined with the default deictionaries (=> if one key forgotten, it will be set to the default value)
        self.goods:dict[str, int] =        goods | Player.DEFAULT["goods"]                  # the goods currently owned
        self.technologies:dict[str, int] = technologies | Player.DEFAULT["technologies"]    # the technologies currently owned




class Pasture(Building):
    def __init__(self, x:any, y:any, village:Village, lvl:int = 1):
        super().__init__(x, y, "pasture")
        self.x:any           = x                # x-coordinate of the pasture     #!!! => change x and y to tuple (x, y)
        self.y:any           = y                # y-coordinate of the pasture
        self.village:Village = village          # #!!! the village the pasture is part of/belongs to
        self.owner:Player    = village.owner    # the owner of the pasture #!!! => actually needed? can be accessed via village
        self.lvl:int         = lvl              # the level of the pasture

    def produce(self):
        # pasture produces wool (amount: multiplication of the level of the village and the level of the pasture)
        self.owner.goods["wool"] += (self.lvl * self.village.lvl)

    def klick(self, player:Player): # !!! player not used
        # when klicked on, the sidebar for the pasture is returned (to e.g. upgrade the pasture)
        return sidebar.pasture(self)












# Button-Class (like a buttons-template)
class Button(arcade.Sprite):
    def __init__(self, f:str, h:any):
        super().__init__("data/buttons/" + f + ".png", center_x = 890, center_y = h*84 - 10)
        self.f:str = f              # the Button-Image-Name
        self.type:str = "Button"    # the type of Sprite (= Button)


# Text-Class (like a text-template)
class Txt(arcade.Text):
    def __init__(self, txt:str, x:any, y:any, color:any, b:bool = False):
        super().__init__(txt, x, y, color, font_name="data/fonts/minimalistic.ttf", font_size = 16, bold = b)
        self.type:str = "Txt"       # the type of Sprite (= Text)


# Image-Class (like an image-template)
class Img(arcade.Sprite):
    def __init__(self, file:str, x:any, y:any):
        super().__init__(file, scale= 2, center_x = x, center_y = y)
        self.type:str = "Img"       # the type of Sprite (= Image)





SCREENWIDTH  = 1000
SCREENHEIGHT = 840



sp = Suchspiel(SCREENWIDTH, SCREENHEIGHT, "NATIONWARS", 24, 24)
arcade.run()



# IMPORTANT NOTE: #!!!!!! TODO DANIEL => FINISH