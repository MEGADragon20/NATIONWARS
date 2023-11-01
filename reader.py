def getvars():
    vars = []
    num = ""
    # Use a raw string to specify the file path
    with open(r'data/worlds/worldmap.csv') as f:
        for line in f:
            num = line.strip()  # Remove newline character
            vars.append(num)
    return vars