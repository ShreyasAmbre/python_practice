# Refer Point 5 in Advance Notes on Python
class Student:
    # Below are Class property
    school = "St. Xavier's High School"

    def __init__(self, name, std):
        # Below are object property
        self.name = name
        self.std = std

    # Object methods
    def student_details(self):
        print("Details is :- ", self.name, self.std)

    # 2 types of object methods
    # Below is Accessor Methods :- used to access method
    def getName(self):
        return self.name

    # Below is Mutators Methods :- used to set the new value to object property
    def setStd(self):
        self.std = "HSC"
        return self.std

    # Below are class methods class decorator is initialized
    @classmethod
    def getSchool(cls):
        print(cls.school)

    # Below are Static Methods and static decorators are initialized
    @staticmethod
    def info():
        print("Hiii I m static methods")


s1 = Student("Shreyas", "SSC")

# Object methods are called like this using object name
s1.student_details()

# Class Methods is called like this using class Name
Student.getSchool()

# Static Methods are called like below using class name
Student.info()

# calling accessor methdos
name = s1.getName()
print(name)

# calling set methods
update_std = s1.setStd()
print(update_std)

s1.student_details()