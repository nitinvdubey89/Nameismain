zzz = 8

def new_scope():
    zzz = 10
    print(f'this my local {zzz}')

new_scope()
print(zzz)


def my_function(a,b):
    print(f'a is {a}')
    print(f'b is {b}')

my_function(10, 5)  # positional arguments 
# if i call more or less arguments , i will get  typeerror: takes 2 positions but give x




def my_function1(a,b= 20):
    print(f'a is {a}')
    print(f'b is {b}')

my_function1(10, 5) # we can have 5 also skip 5
my_function1(10)

#def my_function2(a,b= 20 , c):
 #   print(f'a is {a}')
 #   print(f'b is {b}')
#my_function2(5, 30 ) 
# 30 will be not be assigned to b or c as the rule is no-default argument will be assigned to default argument



def my_function3(a,b= 20 , c=9):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'c is {c}')


my_function3(5, 30) # 30 will be assigned to b


## if i want to assign value for the first and the third argument but omit the second argument
# keyword argument allow us to ignore the order in which the parameter is defined
# we can also skip those arguments

my_function3(b=5, a=6, c=7) #these are keyword arguments

# first specify the positional argument and then the keyword argument

my_function3(6, c = 1 , b =9 )

#my_function3(a=6, 1 , b =9 ) ## positional argument is not allowed to follow a  keyword argument

#my_function3(6, b=1, 9) # this is also not possible becasue after b=1 we need to define  c=9

## sum that calculates n number of numbers i.e. we dont nkow the number of arguments

def f1(a, *args):  # args is a tuple
    print(f'a: {a}')
    print(f'args: {args}')
    s = a + sum(args)
    print(f'Sum:{s}')

def f2(**kwargs): # kwargs is a dictionary
    print(kwargs)
    if 'name' in kwargs:  # name should be in ''
         print(f'Your name is {kwargs["name"]}')

f1(5)
f1(5,4)
f2(name='John', age=40, location='London')


### kwargs  , now instead of positional arguments we need to use keyword argument then we should use kwarg


### also rememeber that the names args and kwargs are 
# just conventions we can use * for positions and ** for keyword arguments
##

def f3(**x): # kwargs is a dictionary
    print(x)
    if 'name' in x:  # name should be in ''
         print(f'Your name is {x["name"]}')

f2(name='rahul', age=40, location='London')


t1 = tuple(range(100)) #tuplpe and range are built-in functions # range is 0 to 99
print(t1) # global space variable t1

print(x)  # a name error, python will look for global or module namepsca or built in namespce and return run time error




