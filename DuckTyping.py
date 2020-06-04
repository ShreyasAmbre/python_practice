# Go through code sowly to understand Duck Typing :- It is basically One Object can perform different methds of
# different class but methods names should be same  object creation class should me mention properly from where we
# want to perform the methods


class PyCharm:
    def excecute(self):
        print("Compile")

class Sublime:
    def excecute(self):
        print("Compile")
        print("Run")
        print("Debug")

class Laptop:
    def code(self, obj1):
        obj1.excecute()

obj1 = Sublime()
# obj1.excecute()

l1 = Laptop()
l1.code(obj1)