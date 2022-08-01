## in order to define a class , we use the class keyword
class Robot:   # camel case convention
     def __init__(self,name, year): # self is the first paramter i.e. the self keyword
            self.name = name # self connects to the instance of the class i.e. object that calls the methods, its the instance of the object itself
            self.year = year ####


"////This class implements a robot "
                 #pass

r1 = Robot("nitin",1999)

print(type(r1))

print(r1.__doc__)

## lets add functionality to our class, attributes to orobot
### __init__ class constructor
## method is a function defined inside a class
## it wil lbe calls
# any time we create a new instance of a class, python will look for __init__ method
## this method is called automatically
## its optinal method

