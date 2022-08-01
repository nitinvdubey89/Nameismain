# a decorator is high order function that takes another function as an argument and extends or decorates the behaviour
# of the later function without explicitly modifying it amd also decorator returns the function

# when to use decorator
# when we have a function that does simple stuff and in time we need to add more funcitonality or code to our functino
# maybe sometime we want to call the original function without the extra features that have been added
# another approach is to create a brand new function and copy paste the code of the orginal function and add other features in the new function
# thou this works we unnecsaary repreat the code
# the python solution to this problem is called decorator and its an on and off switch
# we add to our function that activates and deactivates differente things in our function
# decoraator allow us  perform some operation before calling the function , they simplify the code

# application tht checks the perimission a user has and based on those perimission and applicaiton executeds a taks or another
# it can be a record from database as well

user = {'username':'js','level': 'guest'}

def user_has_permissions(func): ## this is a decorator i.e. takes function as a argument and returns a function
    def wrapper_user_has_permission():
        if user['level'] == 'admin':
         return func
        else:
         return None #    print(my_function()) ## her we are using my_function() with ()
                       #TypeError: 'NoneType' object is not callable
    return wrapper_user_has_permission

def show_pass():  ## we notice how we chanhed the behavior of show pass without changing the show pass function
    return 'asabssuan'

my_function = user_has_permissions(show_pass) ## after writing the user_has_permission always returns a function
                                                # hence we can call the function withut this test

print(my_function())

## below statements are only required when we are not returning the function  i.e. we are not using wrapper_user_has_permission
if type(my_function) == "<class 'NoneType'>":
    print(f'{my_function()} is good') ## her we are using my_function() with ()
else:
    print('No access!')

    # decorators are majorly used in flask and uses decorator extensively with elegant and intuitively code
    #  inner function is known as the wrapper function adn the decorator will return the inner function plus the free variables
    # decorator returns a closure
    