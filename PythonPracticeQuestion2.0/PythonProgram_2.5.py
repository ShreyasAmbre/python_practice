# Write a Python function that takes a list of words and returns the length of the longest one.
l = ["apple", "banana", "cherry", "watermelon", "mango"]
l2 = []
for i in l:
    wrdlen = len(i)
    l2.append(wrdlen)
    print(l2)

print(max(l2))
