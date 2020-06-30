def myfunc(n):
    print("***")
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
