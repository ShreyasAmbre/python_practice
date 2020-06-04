# Print Histogram
# [2, 1, 3, 4]
# output :- @@
#           @
#           @@@
#           @@@@
l = [2, 1, 3, 4]
for a in l:
    i = 1
    while i <= a:
        print("@", end="")
        i += 1
    print()
