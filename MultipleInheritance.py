# Multiple Inheritance

class Parents:

    def __init__(self, fathername, mothername):
        self.fathername = fathername
        self.mothername = mothername

    def giveBirth(self):
        print("My mother", self.mothername, "give me birth")

    def taught(self):
        print("My father", self.fathername, "teach me lot")


class GrandParent:

    def __init__(self, gfathername, gmothername):
        self.grandfather = gfathername
        self.grandmother = gmothername

    def takeCare(self):
        print("My Grand Parent", self.grandfather, self.grandmother, "takes care of my self")


class Child(Parents, GrandParent):

    def __init__(self, name, father, mother, grandfather, grandmother):
        # Below we use class name when we want to inherit two contructor
        Parents.__init__(self, father, mother)
        GrandParent.__init__(self, grandfather, grandmother)
        self.name = name

    def childetails(self):
        print("My Name", self.name)
        print("My Parents", self.fathername, self.mothername)
        print("My Grand Parents", self.grandfather, self.grandmother)


child1 = Child("Shreyas", "Shirkant", "Sujata", "Jijaba", "Laxmi")

child1.childetails()
