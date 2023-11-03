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