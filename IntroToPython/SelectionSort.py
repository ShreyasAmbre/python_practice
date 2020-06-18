l = [5, 3, 8, 6, 7, 2]

for i in range(5):
    mv = i
    for j in range(i, 6):
        if l[j] < l[mv]:
            mv = j
            
    temp = l[mv]
    l[mv] = l[i]
    l[i] = temp
    print(l)









