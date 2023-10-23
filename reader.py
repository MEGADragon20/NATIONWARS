def getvars():
    vars = []
    num = ""
    # Use a raw string to specify the file path
    with open(r'data/worlds/worldmap.csv') as f:
        for line in f:
            num = line.strip()  # Remove newline character
            vars.append(num)
    return vars

def returnvars(rvars):
    # Use a raw string to specify the file path
    with open(r'C:\Users\ferna\OneDrive\Dokumente\GitHub\Programme\002_GEMISCHTE_AUFGABEN\10_arcade\NATIONWARS\data\worlds\classic.csv', "w") as f:
        for i in rvars:
            f.write(str(i) + "\n")