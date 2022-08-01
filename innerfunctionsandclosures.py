def outer():
    msg = 'Python' #free variable for the inner funciton
    x = 1
    y = 1
    def inner():
        print(f'{msg} is really cool!')
        nonlocal x # if i dont declare x as non local then i will get an error , local variable x referrenced before assignement
                   #use of nonlcal is similar to global keyword i.e. nonlocal is used to declalre a variable
                   # inside a nested function is not local to ir
                   # meaning it lies in the outer enclosing function
        nonlocal y #=  10 ## this is a local variable is created inside the nested function and it will alwyas print out 11
        x += 1
        y += 1
        print(x)
        print(y)  ## value of y is not saved between function calls
    #inner()
    return inner # when we return a function , we dont need paranthesis
                 # this is what high order function , we dont really only thr function bit also its free variable

fn = outer()  # fn is the closure
fn()
print(fn.__code__.co_freevars)

fn()

# closure saves the state and values of nonlocal variables between calls

# in python all local variables like msg are going out of scope , in python all variable local to a function are destroyed
# and not accessible after the function has finished the execution
# then how outer was able to print the configuration
# this is because of the closure which captured the valie of that variable
# the closure still has the value when outer finished execution  i.e as a conclusion , closure is inner function + extended scope that contains
#the non local or free variable
# free varibale is a must to do the closure

## then inner function is created only when calling outer , not when outer is created
# .Outer body is created only when outer is called.
# the variable msg is called non local or free variable for the inner funciton
#

# we can get list of all free variable of the closure in form of a tuple
print(fn.__code__.co_freevars)


#Hello and welcome back.#In a recent lecture, we'll talk about inner functions and closures of function defined inside.#Another function is called nested or inner function.
# #Inner functions can access the variables of the enclosing scope.#Lexia an example.
# #I am defining a new function simply called outer.#Inside the function, I am declaring a local variable, Ms.
#G equals, and the string python inside the outer function, we define another function that references
#the MSG variable, D.F. Inner.
#This is the name of the function and I'll point out the MSG variable.
#Ms between curly braces is really cool.
#And after defining the inner function, we call it.
#I'm going to call the outer function and then run the script.
#And it pointed out Python is really cool.
#Now let me explain what happens behind the scenes.
#The inner function is created only when calling out or not.
#When outturn is created, the outer body is executed only when outer is called.
#The variable MSG is called nonlocal or free variable for the inner function.
#Now we'll try something different instead of calling in or inside the outer function, we retargeted.
#So he turned in without calling the function, so without parentheses.
#We've seen in the last lecture that it's perfectly legal to function from another function.
#This is what high order function means.
#What happens when we return inor we don't return only the function, but also it's very variable called
#MSgt.#This is referenced inside the Viña function.
#When we return, Inner, we return, in fact, a closure, which is the inner function, plus its own
#nonlocal variables.#In this case, there is only one variable MSJ.
#Let's assign if N equals outr now, if N is the closure and if we on it, we get the String Bethanie#school.
#Let's call if and and I'm writing the script.#And I've got the same string before any school.#Does it seem weird to you?
#Let's think for a minute when we write, if N equals the python executes outer and when it finishes
#the execution, all its local variables like MSG, are going out of scope.
#Yeah, in Python, all variables, local to a function are destroyed and not accessible anymore after
#the function has finished its execution.
#So how is it possible to have access to major variable after Outr went out of scope so after it has
#finished its execution?
#And the answer is that this is because of the closure which captured the value of that variable, so
#when Outr finishes running, the closure still has that value.
#It's a conclusion you can think of, a closure is an inner function plus an extended scope that contains
#the nonlocal or three variables.
#At least every variable is a must to create a closure.
#By the way, we can get a list of all free variables of the closure in form of a table like this, if
#in that Dundar code, that code underline free verse.
#This statement will point out the free variables.
#And there is only one MSgt.
#If you want to modify a nonlocal or a free variable inside of the closure, you declare that a variable
#nonlocal before changing it.
#For example, X equals one, and inside the Weimar function, I write nonlocal X, then I can modify
#X, for example, X plus equals one print X.
#We see that the value of X is to.
#If I don't declare X nonlocal, I'll get another.
#Unbound local air, local variable X referenced before assignment.
#We've discussed about this in the scope lecture.
#The use of nonlocal kirp is very much similar to the global keyword, nonlocal is used to declare that
#a variable inside a nested function is not local to it, meaning it lies in the outer enclosing function.
#If and is a function in there, it doesn't function, so we can call it.
#And I've done this on the line 14, let's call it again.
#And the new value of X is three.
#Let's call Ifan again.
#Now, the value of X is four, and we noticed that a closure saves the space and to the values of nonlocal
#variables between calls.
#One more detail, if I don't declare X nonlocal and be right, X equals, then a local variable to a
#name is created inside the nested function.
#So it will always print out 11.
#The value of X is not saved between functions calls.

