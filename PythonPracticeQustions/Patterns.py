print("Patterns")

# Patter 1
for a in range(4):
    print("*", end="")
    for b in range(3):
        print("*", end="")
    print()


# pattern 2
i = 3
for a in range(4):
    print("a", end="")
    for b in range(i):
        print("b", end="")
    i = i - 1
    print()

# Patter 3
i = 0
for a in range(4):
    print("a", end="")
    for b in range(i):
        print("b", end="")
    i = i + 1
    print()