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

    def add(self,money,skills,enthalten):
        if enthalten(self.parrents)==True:
            if money >= self.preis:
                if self.civ == "j":
                    erforscht.update({self.name:self})
                    print(self.name)
                    return
        print("error")


