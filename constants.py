import sys

RAHUL = 4
satish = 1
#Python doesn't have constants.21 Apr 2010
#Use all capital letters in the name: First and foremost, you want your constants to stand out from your variables.
#Do not overly abbreviate names: The purpose of a constant — really any variable — is to be referenced later.
RAHUL = satish + 1
print(RAHUL)
sys.getsizeof(RAHUL) # number of bytes

#####################
## Variables in Python
#####################

# defining variables
miles = 10  # type integer
name = 'John'  # type string (because the value of the variable is between single quotes)
a, b, c = 1.5, 3, 'x'  # defining 3 variables on the same line (a float, an integer and a string)

max_permitted_value = 500  # snake-case notation. PEP 8 recommends using snake case for variable names
maxPermittedValue = 500  # camel-case notation

# Illegal or not recommended names
# 4you = 10  #illegal name, it starts with a digit
# valu!es = 100 #illegal name, it contains special characters
# str = 'Python'  #not recommended name, str is a Python language keyword
# _location = 'Europe' #not recommended name. Avoid names that start with underscores (they have special meaning)


#####################
## Comments in Python
#####################

# this line is a comment. Comments in Python start with the hash character, #, and extend to the end of the physical line.
# If you want to comment out more lines, insert a hash char at the beginning of each line

# the following line is commented out and ignored by Python Interpreter
# x = 1

a = 7  # defines a variable that stores an integer

my_str = 'A hash character # within a string literal is just a hash character.'

#########################
## Built-in Data Types
#########################

age = 31  # type integer

miles = 3.4  # type float

finished = True  # type boolean

name = 'Andrei'  # type str (string)

years = [2018, 2019, 2020]  # type list

week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')  # type tuple

vowels = {'a', 'e', 'o', 'u'}  # type set

fs = frozenset((1, 2, 'abc', 'xyz'))  # type frozenset

countries = {'de': 'Germany', 'au': 'Australia', 'us': 'United States of America', 'gr': 'Greece'}  # type dictionary

#############################
## Numbers and Math Operators
#############################

a = 9
b = 4
## Arithmethic Operators
a + b  # addition operator => 13
a - b  # substraction operator => 5
a * b  # multiplication operator => 36
a / b  # division operator => 2.25
a // b  # floor division operator => 2
5.0 // 3.0  # => 1.0 # works on floats too
a ** b  # exponentiation operator (a to the power of b) => 6561
a % b  # modulus operator => 1

## Assignment Operators
a = 5
a += 2  # Shorthand for a = a + 2 => a = 7
a -= 3  # Shorthand for a = a - 3 => a = 4
a /= 2  # Shorthand for a = a / 2 => a = 2
a *= 3  # Shorthand for a = a * 3 => a = 6
a **= 2  # Shorthand for a = a ** 2 => a = 36

## Arithmethic Built-in Function
divmod(9, 4)  # returns the quotient and remainder when using floor(integer) division => (2, 1)
sum([1, 2, 4])  # returns the sum of an iterable => 7
min(1, -2, 3)  # returns the minimum value => -2
max(1, 2, 4)  # returns the maximum value => 4
a = 10 / 3  # a = 3.3333333333
round(a, 4)  # returns a number rounded with 4 decimals => 3.3333
pow(2, 4)  # 2 ** 4 = 16

######################################
## Comparison and Identity Operators
######################################

# Assignment is =
a = 2
b = 3

# Equality is == and compares the values stored by the variables
a == b  # => False
b == b  # => True

# Inequality is !=
a != b  # => True

# More comparisons
a > b  # => False
5 >= 5  # => True
b <= a  # => False

'Python' == 'python'  # => False - case matters

id(a)  # => returns the address where the value referenced by a is stored 140464475242000

# is checks if two variables refer to the same object (saved at the same memory address)
a is b  # => False = compares the address of a to the address of b

#################################
## Boolean Variables
#################################

## True equals 1 and False equals 0
True == 1  # => True
bool(True)  # => 1

False == 0  # => True
bool(False)  # => 0

1 is True  # => False
0 is False  # => False

True > False  # => True
a = (True + True) * 10  # => 20

id(True)  # => 10714848 (you'll optain another value)
id(4 > 2)  # => 10714848  - the address of True and False is constant during program execution

# The next 2 expressions are equivalent
(4 > 2) == True  # => True
(4 > 2) is True  # => True

## Truthiness of objects
bool(0)  # => False
bool(0.0)  # => False
bool(10)  # => True
bool(-1.5)  # => True

bool('')  # => False (empty string)
bool('py')  # => True

bool([])  # => False (empty list)
bool([1, 2])  # => True

bool(())  # => False (empty tuple)
bool((3, 4))  # => True

bool({})  # => False (empty dictionary)
bool({1: 'abc', 2: 55, 'a': 5})  # => True

#################################
## Boolean Operators
#################################
# exp1 and exp2 -> True when both expressions are True and False otherwise
# exp1 or exp2  -> True when any expression is True


a, b = 3, 5

a < 10 and b < 10  # => True
a < 10 and b > 10  # => False

a < 10 or b < 10  # => True
a < 10 or b > 10  # => True

# The next 2 expressions are equivalent
2 < a < 6
a < 2 and a < 6  # more readable

a != 7 or b > 100  # => True

not a == a  # => False
a == 3 and not b == 7  # => True

not a > 10 and b < 10  # => True

a < 10 or b > 10  # => True
not a < 10 or b > 10  # => False
not (a < 10 or b > 10)  # => False

# !!!!!!!!!!!
# Python considers in fact 4 > 2 and 2 == True.
4 > 2 == True  # => False
(4 > 2) == True  # => True