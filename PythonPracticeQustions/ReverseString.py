print("Reverse String")

name = "Shreyas"
l = list(name)
print(l)

collection = []
n = len(l) - 1
for a in l:
    collection.append(l[n])
    n = n - 1

final_output = str(collection)
print(final_output)

# Other Simple Method
slicedString=name[::-1] # slicing
print (slicedString) # print the reversed string

# ANother Methods

for b in name[::-1]:
    print(b, end="")