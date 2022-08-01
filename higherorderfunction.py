
def sum(number, fn):
       result = 0
       for n in range(1, number+1):
              result  += fn(n)
              print(id(result))
       return result

def square(x):
    return x**2

sum(3, square) ## square without parenthesis is the variable
result = sum(3, square)
address1 = id(result)
print(result)
print(address1)


import math
result = sum(10,math.sqrt)
print(result)
print(id(result))

def compute(msg):
       if msg == "sqaure":
              return square
       else:
           return math.sqrt

func = compute("square")
print(type(func))
print(func(10))

fn = compute("x")
print(fn(25))