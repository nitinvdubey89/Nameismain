from typing import List, Optional

class Student:
     def __init__(self, name: str, grades: Optional[List[int]] = None): # this is bad , never make a parameter as mutable object
         self.name = name
         self.grades = grades or [] #none and empty list will evaluate to empty list

     def take_exam(self, result: int):
         self.grades.append(result)


bob = Student("Bob", [13,14])
rolf = Student("rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)