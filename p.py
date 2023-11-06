lis = ["1", "23", "12", "100", "56", "3", "0", "44", "00"]
print(lis)
empty = []
for i in lis:
    print("##")
    print(i)
    if len(i) == 1:
        i = "00" + i
        print("->")
        print(i)
    elif len(i) == 2:
        i = "0" + i
        print("->")
        print(i)
    empty.append(i)
lis = empty
print("______________")
print(lis)