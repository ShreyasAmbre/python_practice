print("Will learn about class and object")


class Computer:
    # Their are 2 types of variables i.e:- object variable which is created is __init__() method,
    # class variable (known as static variable)

    # Static variable same for all object created using this class
    manufacturedIn = "China"

    # below is property initialization method __init__() it get called when object is created
    # power & memory are normal arguments which we get assign to object
    # in 'self' object we get pass automatically explained below
    def __init__(self, cpu, ram):
        # below self is object.cpu = power i.e:- assigning argument value to object
        self.cpu = cpu
        self.ram = ram

    # Below is method, What is self? explaind below
    def config(self):
        print("Config is :- ", self.cpu, self.ram)


# Object of class is created
c1 = Computer("i3", "16 RAM")

'''As we see config as paramater self but below we dont pass anything, How it works? & WHat is self ?
What is self :- self is pointing to object of that class that is c1 object created above of class Computer
How it works? :- Behind the seen that object is pass as a paramter of config(c1)'''
c1.config()
print(c1.manufacturedIn)
print(Computer.manufacturedIn)
# Below statement will also work as per above explaination
Computer.config(c1)
