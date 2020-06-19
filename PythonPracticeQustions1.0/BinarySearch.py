list = [2, 12, 15, 23, 30, 56, 89, 91, 93, 95, 100]
n = 95

lower = 0
upper = len(list) - 1

while lower < upper:
    mid = (lower + upper) // 2
    if list[mid] == n:
        print("Number Found at", mid)
        print("Number Found at", mid)
        break
    else:
        if list[mid] > n:
             upper = mid
        else:
            lower = mid
