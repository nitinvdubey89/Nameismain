#Python super()
#One of the important OOP features is Inheritance in Python.
# When a class inherits some or all of the behaviors from another class is known as Inheritance.
# In such a case, the inherited class is the subclass and the latter class is the parent class.

#In an inherited subclass, a parent class can be referred to with the use of the super() function.
# The super function returns a temporary object of the superclass that allows access to all of its methods to its child class.



#Furthermore, The benefits of using a super function are:-
#Need not remember or specify the parent class name to access its methods.
# This function can be used both in single and multiple inheritances.
#This implements modularity (isolating changes) and code reusability as there is no need to rewrite the entire function.
#Super function in Python is called dynamically because Python is a dynamic language unlike other languages.


class Animals:

    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True

    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")

    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")


class Dogs(Animals):
    def __init__(self):
        super().__init__()

    def isMammal(self):
        super().isMammal()


class Horses(Animals):
    def __init__(self):
        super().__init__()

    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")


# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()

#Super function in multiple inheritance

#Example: Let’s take another example. Suppose a class canfly and canswim inherit from a mammal class and these classes
# are inherited by the animal class. So the animal class inherits from the multiple base classes.
# Let’s see the use of super in this case.


class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)


class canSwim(Mammal):

    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)


class Animal(canFly, canSwim):

    def __init__(self, name):
        # Calling the constructor
        # of both the parent
        # class in the order of
        # their inheritance
        super().__init__(name)


# Driver Code
Carol = Animal("Dog")

