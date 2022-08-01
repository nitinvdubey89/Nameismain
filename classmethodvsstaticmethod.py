#Class method vs Static method in Python

#Class Method
#The @classmethod decorator is a built-in function decorator that is an expression that gets evaluated 
# after your function is defined. The result of that evaluation shadows your function definition.
#A class method receives the class as an implicit first argument, just like an instance method receives the instance

#A class method receives the class as an implicit first argument, just like an instance method receives the instance
import pydoc_data.topics


class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
#fun: function that needs to be converted into a class method
#returns: a class method for function.


#A class method is a method that is bound to the class and not the object of the class.
#They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
#It can modify a class state that would apply across all the instances of the class.
# For example, it can modify a class variable that will be applicable to all the instances.

#Static Method

#A static method does not receive an implicit first argument.


class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
       # ...
returns: a static method for function fun.


#A static method is also a method that is bound to the class and not the object of the class.
#A static method can’t access or modify the class state.
#It is present in a class because it makes sense for the method to be present in class.
#In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
#We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

#When to use what?

#We generally use class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
#We generally use static methods to create utility functions.

#How to define a class method and a static method?
#To define a class method in python, we use @classmethod decorator, and to define a static method we use @staticmethod decorator.
#Let us look at an example to understand the difference between both of them. Let us say we want to create a class Person. Now, python doesn’t support method overloading like C++ or Java so we use class methods to create factory methods. In the below example we use a class method to create a person object from birth year.
#As explained above we use static methods to create utility functions. In the below example we use a static method to check if a person is an adult or not.

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    #@classmethod
    def fromBirthYear(self, name, year):
         return cls(name, date.today().year - year)
    #def fromBirthYear(self,name,year):
     #   age = date.today().year - year
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
#person2 = Person.fromBirthYear('mayank', 1996)

print(person1.fromBirthYear(1996))
#print(person2.age)

# print the result
print(Person.isAdult(22))

21
25
True