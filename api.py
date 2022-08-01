l  = ['nitin', 'rahul', 'rohit']
t = ('nitin', 'rahul', 'rohit')
s = {('nitin', 'rahul', 'rohit')}
print(s)


s = l.__add__(['nitin','ravi','ramesh'])
print(s)

l.append('nitin')
print(l)

l.remove('nitin')
print(l)

friends ={'vibhor', 'reena', 'divya'}
abroad = {'reena','ramesh'}
print('''###############################################
      \n##########''')
local_friends = friends.symmetric_difference(abroad)
print("hellp ", local_friends)
local_friends = friends.difference(abroad)
print("hellp oo",local_friends)
print("#########################################################")


local_friends = abroad.difference(abroad)
print(local_friends)

friends_new = friends.union(abroad)
print("this is union",friends_new)

art  = {"bob","Jen", "Rolf", "Charlie"}
science = {"BOB", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)
## The symmetric difference of two sets A and B is the set of elements that are in either A or B,
# but not in their intersection.
print(art.symmetric_difference(science))
#   The difference_update() updates the set calling difference_update() method with the difference of sets.
# the update function does an inplace change and the non symmetric does not do in place chaneg
A = {'a', 'c', 'f','g', 'd'}
B = {'c', 'f', 'g'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z  = x.difference_update(y)
print(type(z))

result = A.difference_update(B)
print(result)
print("this is a differnence update", result)
print('A = ', A)
print('B = ', B)
print('result = ', result)

#Return Value from symmetric_difference_update()
#The symmetric_difference_update() returns None (returns nothing). Rather, it updates the set calling it.

A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }

result = A.symmetric_difference_update(B)
print('''##########''',result)
print('A =', A)
print('B =', B)
print('result =', result)

#The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.

#Two sets are said to be disjoint sets if they have no common elements. For example:

##A = {1, 5, 9, 0}
##B = {2, 4, -5}

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))


#The issubset() method returns True if all elements of a set are present in another set (passed as an argument).
# If not, it returns False.
#Set A is said to be the subset of set B if all elements of A are in B.


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))
print("########################################################################")
#The any() function returns True if any element of an iterable is True. If not, it returns False.

boolean_list = ['True', 'False', 'True']

# check if any element is true
result = any(boolean_list)
print(result)

# Output: True

# At east one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))

#In the case of dictionaries, if all keys (not values) are false
# or the dictionary is empty, any() returns False. If at least one key is true, any() returns True.

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))

# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))

print(("################### ALL FUNCTION ###################################"))
# all values true
l = [1, 3, 4, 5]
print(all(l))

print("# all values false")
l = [0, False]
print(all(l))

print("# one false value")
l = frozenset([1, 3, 4, 0])
print(all(l))

q = l.copy()
print(type(l))
print(id(l))
print(id(q))
print("# one true value")
l = [0, False, 5]
print(all(l))

print("# empty iterable")
l = []
print(all(l))


print("################## ascii #######################################")
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')


print("######## Bin function")
number = 5
print('The binary equivalent of 5 is:', bin(number))
###################

#Convert an object to binary implementing __index__() method


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))

#The bytearray() method returns a bytearray object which is an array of the given bytes.




print("# convert list to bytearray")

prime_numbers = [2, 3, 5, 7]
print(prime_numbers)

byte_array = bytearray(prime_numbers)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')
#bytearray() method returns a bytearray object
# (i.e. array of bytes) which is mutable (can be modified) sequence of integers in the range 0 <= x < 256.

#bytearray([source[, encoding[, errors]]])

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

size = 5

arr = bytearray('1', 'utf-8')
print(arr)

rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)


x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))
class Foo:
  def __call__(self):
    print('Print Something')

print(callable(Foo))

class Foo:
  def __call__(self):
    print('Print Something')


InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()

class Foo:
  def printLine(self):
    print('Print Something')
print(callable(Foo))

message = 'Python is fun'

# convert string to bytes
byte_message = bytes(message, 'utf-8')
print(byte_message)

# Output: b'Python is fun'

#bytes([source[, encoding[, errors]]])


string = "Python is interesting."


# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)


size = 5

arr = bytes(size)
print(arr)


rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)


#The chr() method returns a character (a string) from an integer (represents unicode code point of the character).

print(chr(97))
print(chr(65))
print(chr(1200))

try:
  print(chr(-1))
except Exception as e:
    print(e)

#The getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.

class Student:
  marks = 88
  name = 'Sheeran'

person = Student()

name = getattr(person, 'name')
print(name)

marks = getattr(person, 'marks')
print(marks)

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)


class Person:
    age = 23
    name = "Adam"
person = Person()
# when default value is provided
print('The sex is:', getattr(person, 'sex', 'Male'))
# when no default value is provided
try:
 print('The sex is:', getattr(person, 'sex'))
except Exception as e:
 print(e)
 #The globals() method returns the dictionary of the current global symbol table.
#A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.
#These include variable names, methods, classes, etc.
#There are mainly two kinds of symbol table.
#Local symbol table
#Global symbol table
globals()
age = 23
globals()['age'] = 25
print('The age is:', age)
