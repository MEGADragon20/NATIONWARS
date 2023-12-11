liste = ["cock", "hen", "crap"]

def next(shit: list):
    b = shit[0]
    shit.pop(0)
    shit.append(b)
    return shit

print(next(liste))