#Let's move on and see a possible problem introduced by decorator's.
#This new problem is related to introspection.
#Do you know what introspection is?
###OK, let me tell you, introspection is the ability of an object to know about its own attributes at
#ru#ntime, for instance, a function knows its own name and documentation.
#Le#t's remove the part that degrades the function.
#So this is a normal function.
#It's not connected to the decorator anymore.
##And let's point out the documentation and the name of the function like this print remove file that
#underline, underline, underline, underline
#By the way, this is pronounced Dundar Doc.
##And the name of the fine print remove file, the function that Dundar name, and I'm executing the script.
#And we've got the expected result, this is the dog's drink and this is the function name perfect.
#Now let's add back the ate only admin part.
##We decorate the function again and I'll execute the script again.
#And surprise, we've got other values for the underdog and the Dunbar name.
#When writing the script, we noticed that we get none and proper only admin.
#In fact, this is the dog straying into the name of the proper function.
#Remember that decorating afunction means surrounding the function is an argument of the decorator function
#and assigning it back to the same label called the decorated function.
#So in this example, Danta Doc and the Danda name are the docs think, and the name of the wrapper function,
#the function that is returned by the decorator.
#Just to prove that I'll add a string to the wrapper function.
#I have executed the script and we can notice that the doctrine of the proper function has been pointed
#out.
#OK, now the question is, how can we preserve the name and the doctrine of our decorated function?
#When you write remove file that Don Bardock and remove file under name, you expect that the string
#end to the name of the remove file function.
#To overcome with these decorator's should use the ET funk tools that ROPS decorator, which will preserve
##information about the original function.
#The first step is to impart the functional module and then before the proper function, we write at
####Fong-Torres that wraps of funk.
#In #fact, we are decorating the proper function.
#Import Fong-Torres.
#And I am decorating the proper function, func tools that wraps and the name of the function that it
#takes is argument.#
#In this case it's func.
#Let's execute the script.
#And it's much better we see the dogs stepping into the name of our decorated function is expected.
#You do not need to change anything about the decorated remove file function.
#This is especially useful when using libraries or frameworks that use decorators and to look for the
#name of the function using the tanda name notation.



import functools


def my_new_decorator(just_a_func):
    @functools.wraps(just_a_func)  # preserving __name__ and __doc__
    def wrapper_my_new_decorator(*args, **kwargs):
        print('Extra code before calling just_a_func()')
        result = just_a_func(*args, **kwargs)
        print('Extra code after calling just_a_func()')
        return result
    return wrapper_my_new_decorator


@my_new_decorator
def just_a_func(x):
    """
    This is the docstring of just_a_func.
    """
    print(f'I\'m just a function. x = {x}')
    return x * x


result = just_a_func(100)
print(f'Returned value result: {result}')

print(f'Function\'s name: {just_a_func.__name__}')
print(f'{just_a_func.__doc__}')

## EXPECTED OUTPUT:
# Extra code before calling just_a_func()
# I'm just a function. x = 100
# Extra code after calling just_a_func()
# Returned value result: 10000
# Function's name: just_a_func
#
#     This is the docstring of just_a_func.