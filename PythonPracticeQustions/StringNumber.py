val = "a3b2i3z4"

for x in val:
    global c
    if x.islower():
        c = x
    if x.isdigit():
        va = int(x)
        for b in range(va):
            print(c, end="")
    # else:
    #     print("String")