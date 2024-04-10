import random

def find_village(d, h, b):
    a = random.randint(0, h - 1)
    b = random.randint(0, b - 1)
    if d[a,b].typ == "grass":
        return d[a,b]
    else:
        return find_village(d, h, b)