l = (22, 12, 89, 66, 52, 14, 32, 15, 86)

# [] list
# () tuple in order and Unchangeable or Immutable No Duplicated
# {"key": value} dictionary unordered Changeable or mutable Allow Duplicated
# {} set is a collection which is unordered and unindexed. No duplicate members.

val = 100

for a in l:
    if val == a:
        print("Number Found")
        break
else:
    print("number not FOund")