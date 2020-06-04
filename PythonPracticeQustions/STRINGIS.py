s = "Shreyas isa cool guy and he isalso simple and sweet"

l = s.split(" ")
print(l)

for a in l:
    if a[0:2] == "is":
        print(a, " :- This string is started with Is")
    else:
        joinstring  = "is" + a
        print(joinstring)

print(l)

