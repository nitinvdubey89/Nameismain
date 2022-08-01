class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        ## reprt and str are speacial methods and alaso called as magic methods

    def __str__(self):
        #return "Hello"
         return f"person is {self.name} and {self.age} years old"

    def __repr__(self): ## repr is not printed but its usually used in debugging
        return f"<person({self.name}),({self.age})>"
bob = Person("BOB", 34)
print(bob)