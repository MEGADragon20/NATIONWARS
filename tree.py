erforscht={}
skills={}
money=100



def enthalten(list):
    ergebnis=True
    for n in list:
        if n not in erforscht.keys():
            ergebnis=False
    return ergebnis        


class Knoten:
    def __init__(self, name, preis, parrents, civ):
        self.name = name
        self.preis = preis
        self.parrents = parrents
        self.civ = civ

    def add(self):
        if enthalten(self.parrents)==True:
            if money >= self.preis:
                if self.civ == "j":
                    erforscht.update({self.name:self})
                    print(self.name)
                    return
        print("error")


skills.update({"Tools": Knoten("Tools", 1, [], "j")})
skills.update({"Mines": Knoten("Mines", 2, ["Tools"], "j")})
skills.update({"Crops": Knoten("Crops", 2, ["Tools"], "j")})
skills.update({"Weapons": Knoten("Weapons", 2, ["Tools"], "j")})
skills.update({"Smithing": Knoten("Smithing", 3, ["Mines"], "j")})
skills.update({"IronMines": Knoten("IronMines", 3, ["Mines"], "j")})
skills.update({"Farms": Knoten("Farms", 3, ["Crops"], "j")})
skills.update({"Foresthuts": Knoten("Foresthuts", 3, ["Crops"], "j")})
skills.update({"Bows": Knoten("Bows", 3, ["Weapons"], "j")})

while True:
    input = int(input(">>"))
    if input == 1:
        skills["Tools"].add()
    if input == 2:
        skills["Mines"].add()
    if input == 3:
        skills["Smithing"].add()
    if input == 4:
        skills["Crops"].add()
    print(erforscht)