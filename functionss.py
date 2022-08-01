def hello():
    print("Hello")

#def user_age_in_seconds(): # definfing
    #user_age = int(input("Enter your age"))
    #age_seconds = user_age *365*24*60*60
    #print(f"Your age in seconds  is {age_seconds}")

#user_age_in_seconds()

default_y = 3

def add(x, y = default_y): # the default_y is taken by the function when the function is first called
    sum = x+y
    print(sum)

add(2)
default_y = 4

add(2)

def add1(x,y):
    print(x+y) # none is the return


# runnig the code

#def print():
   # print()
    #print()
# [Previous line repeated 996 more times]
#RecursionError: maximum recursion depth exceeded
#print()

#5 Types of Arguments in Python Function Definition:
#default arguments.
#keyword arguments.
#positional arguments.
#arbitrary positional arguments.
#arbitrary keyword arguments.

#The function definition starts with the keyword def. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line and must be indented. — python docs


#Formal parameters are mentioned in the function definition. Actual parameters(arguments) are passed during a function call.

#In the below example, the default value is given to argument band c

#def add(a,b=5,c=10):
#    return (a+b+c)
#This function can be called in 3 ways

#Giving only the mandatory argument
#print(add(3))
##Output:18
#2. Giving one of the optional arguments.
#3 is assigned to a, 4 is assigned to b.

#print(add(3,4))
#Output:17
#3. Giving all the arguments

#print(add(2,3,4))
#Output:9

#Note: Default values are evaluated only once at the point of the function definition in the defining scope.
# So, it makes a difference when we pass mutable objects like a list or dictionary as default values.

#2. Keyword Arguments:
#Functions can also be called using keyword arguments of the form kwarg=value.

#During a function call, values passed through arguments need not be in the order of parameters in the function definition.
# This can be achieved by keyword arguments. But all the keyword arguments should match the parameters in the function definition.


#default vs positional vs keyword arguments:
#########################################################################################################################
#1. default arguments should follow non-default arguments

#def add(a=5,b,c):
#    return (a+b+c)

#Output:SyntaxError: non-default argument follows default argument

#################################################################################
#2. keyword arguments should follow positional arguments

#def add(a,b,c):
#    return (a+b+c)

#print (add(a=10,3,4))
#Output:SyntaxError: positional argument follows keyword argument
###########################################################################################
#3. All the keyword arguments passed must match one of the arguments accepted by the function and their order is not important.

#def add(a,b,c):
 #   return (a+b+c)

#print (add(a=10,b1=5,c=12))
#Output:TypeError: add() got an unexpected keyword argument 'b1'
######################################################################################################
#4. No argument should receive a value more than once

#def add(a,b,c):
#    return (a+b+c)

#print (add(a=10,b=5,b=10,c=12))
#Output:SyntaxError: keyword argument repeated
#######################################################################################################

#5. Default arguments are optional arguments

#Example 1: Giving only the mandatory arguments

#def add(a,b=5,c=10):
 #   return (a+b+c)

#print (add(2))
#Output:17


#Important points to remember:

#Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning.
#Use positional-only if you want to enforce the order of the arguments when the function is called.
#Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names.
#Use keyword-only when you want to prevent users from relying on the position of the argument being passed


#Python attributeerror: ‘list’ object has no attribute ‘split’ Solution

#Python TypeError: ‘function’ object is not subscriptable Solution

#Python Recursion: A Guide

#Python List Files in a Directory: Step-By-Step Guide

#if else Python Statements: A Step-By-Step Guide

#Python TypeError: list indices must be integers, not tuple Solution

#Python typeerror: ‘str’ object is not callable Solution

#Remove the First n Characters from a String in Python

#Python beyond top level package error in relative import Solution

#How to Write Python Functions

#Python String to Int() and Int to String Tutorial: Type Conversion in Python

#Python Add to Dictionary: A Guide

# default argument should follow non-default arguments
# keyword arguments should follow positional arguments
# all keyword arguments passed must match one of theh argyments accepted by the function and their order is not important
#no argumet shouyld recieve a value more than once
# defult arguments are optional arguments