list = [4, 7, 8, 12, 45, 99]
val = 45

lower = 0
upper = len(list) - 1
# print(upper)  # 5
mid = (lower + upper) // 2
# print(list[mid])

for i in list:
    if val == list[mid]:
        print("Number Found at", mid)
        break
    elif val < list[mid]:
        upper = mid
        mid = (lower + upper) // 2

    elif val > list[mid]:
        lower = mid
        # print(lower)
        mid = (lower + upper) // 2
    else:
        print("Number not found")









