a = 2
b = 3
# Below we use + symbole to add behind the scene __add__(self, *args, ""kwargs) predefine method get called & get output
# python know what is meaning of + symbol
res = a + b
print(res)


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Now accessing predefine __add__() method and modifying as per our need this in known as OPERATOR OVERLOADING
    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = Student(s1, s2)
        return s3


s1 = Student(12, 6)
s2 = Student(18, 19)

#  Now What if we want to add TWO OBJECT as we know predefine method __add__() works with int datatypes
#  & Student class dont know what is + symbol


# Below + symbol knows what is + it will call above method as Student.__add__(s1, s2)
# 12 + 18 = 30
s3 = s1 + s2
print(s3.m1)

# AS we know in python int is class, str is a class that kniws meaning if + but ur created class does not know what
# is + symbol to make know we use Operator Overloading
