class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

        # Adds an instance variable

    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

    # Driver Code


Rodger = Dog("pug")
Rodger.setColor("brown")
#Dog.setColor(self = Rodger, color = "white")
print(Dog.getColor(Rodger))