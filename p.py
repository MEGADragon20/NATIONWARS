class Pasture(Building):
    def __init__(self, x, y, village, lvl = 1):
        super().__init__(x, y, "pasture")
        self.x = x
        self.y = y
        self.village = village
        self.owner = village.owner
        self.lvl = lvl
    
    def produce(self):
        self.owner.goods["wood"] += (self.lvl * self.village.lvl)
    
    def klick(self):
        return sidebar.pasture(self)