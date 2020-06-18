# n+nn+nnn example input value is 4 then 3+(3*3)+(3*3*3) = 3 + 9 + 27

val = 3
i = 1
res = 0
for b in range(1, val + 1):
    addval = val ** b
    res = res + addval
    print(res)