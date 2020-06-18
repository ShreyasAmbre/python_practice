# Single Inheritance
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def personDetails(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, na, ag, designation, salary):
        # Below statement is used to call all contructors of Parent Class
        super().__init__(na, ag)
        self.designation = designation
        self.salary = salary

    def employeeDetails(self):
        print(self.designation, self.salary)

    def personDetails(self):
        print("HIIII")

        # Parent and Child Constructors are called
    def PersonDetails(self):
        print(self.name, self.age, self.designation, self.salary)


p1 = Person("Shreyas", 23)
e1 = Employee(None, None, "SW Developer", 23000,)

e3 = Employee("Shrikant", 53, "Businessman", 50000)

p1.personDetails()
e1.personDetails()
e1.employeeDetails()

e3.PersonDetails()

