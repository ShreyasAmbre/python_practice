print("Fibonacci Series")
# 1,1,2,3,5,8....
val = 10
a = 1
b = 1
print(a)
print(b)
for x in range(6):
    c = a + b
    print(c)
    a = b
    b = c
