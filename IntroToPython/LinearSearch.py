l = [12, 8, 9, 56, 17, 86]
n = 17


def lsearch(l, n):
    for i in l:
        if i == n:
            return True
    return False


res = lsearch(l, n)
if res:
    print("Numer Found")
else:
    print("Number Not Found")
