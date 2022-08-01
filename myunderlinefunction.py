def  my_function():
    """
    this is my first function
    :return:
    """
    print("Hello pyton world ")

my_function()

help(my_function) # we should not use () for this

print(my_function.__doc__)

##############

def my_new_function(name):
    """
    this is my second function and it prints name
    :param name:
    :return:
    """
    print("Hello Python world" + 'my name is ' + name)

#calling the function

#Parameters vs Arguments

def my_new_param_arg_function():
    # function implementation here

  # In this context a and b are called function  parameters. They are variables local to the function.
  # when we call the function, x and y are called the arguments
  x = 5
  y = 'a_sting'
  my_new_param_arg_function(x,y)

my_new_function("nitin")

#####

def function_name(x,y):
    print(f'1st argument: {x}')
    print(f'2nd argument: {y}')

function_name('Python', 55)


## difference between  a function that prints a message and a function that returns a value
def sum2(a, b):
    sum = a + b
    print(f'sum: {sum}')
    # this function returns implicitlyu a none value as return statemtn is not defined
    # return should be last statmenet and any function after return is not executed

def sum_and_product(a, b):

    sum = a + b
    product = a*b
    return sum, product # return value is lost and we must capture in a variable i.e call the function as a value to a variable
    # return should be last statmenet and any function after return is not executed
    # a function can return many values and in that case it returns a tuple
    print("message after the return statement")

    ## we can also say return a+b, a*b

s, p  = sum_and_product(3, 6)
print(f'Sum is {s} and product is {p}')
s = sum2(4, 6)
print(s)