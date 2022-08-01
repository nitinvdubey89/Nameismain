from datetime import date


class Person:
    def __init__(self,name, age,year):
         self.name = name
         self.age = age
         self.year = year
    # a class method to create a Person object by birth year.
    #@classmethod
    #a = (name,age,year)

    def fromBirthYear(self):
       #return cls(name, date.today().year - year)
       return self.year
    #def fromBirthYear(self,year):
        #self.year = year
       # age = date.today().year - self.year
       # print(age)
    # a static method to check if a Person is adult or not.
    #@staticmethod
    #def isAdult(age):
     #   return age > 18


def fromBirthYear(3):

#a = Person.__init_("nitin",30,1996)
#print(type(a))
person1 = Person('nitin', 20,1996)
person2 = Person('rashmi', 30 ,1982)

print(person1.fromBirthYear())
print(person2.fromBirthYear())

# print the result
#print(Person.isAdult(22))