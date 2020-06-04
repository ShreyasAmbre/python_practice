print("Prime Number Program")

val = int(input("Enter the number"))

i = 2
while i < val:
    if val / i != 0:
        print("Prime")
    i = i + 1