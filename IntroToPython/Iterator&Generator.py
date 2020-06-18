print("Will learn Iterator and Generator")

l = ["Shreyas", "Shirkant", "Sujata", "Ambre"]

# as we know to travel the list, set, dict, tuple, we use for loop
#  But know we have special method in python iter() which will help to travel all element present in list
# next() method is used to print the current value present in iter()
names = iter(l)

print(next(names))
print(next(names))
print(next(names))
print(next(names))


# Generators :- Is Advance version of iter
#               We can create generators it will gives us iterator
#               yield keyword is used to throw the value outside the generators

# yes generato is a function with bracket and no arguments
def topten():
    n = 1
    while n <= 5:
        sq = n * n
        # yield is similar as return keyword but function does not get terminate
        #  yeild will through the value to function generator
        yield sq
        n = n + 1


values = topten()
print(values)
for i in values:
    print(i)
