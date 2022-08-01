#In first-class function, just means that functions
#
#are just variables.
#
#And you can pass them in as arguments to functions and use
#
#them in the same way you would use any other variable.
#
#Let's get started.
#
#Here we have a divide function that raises a zero division
#
#error if the divisor is zero.
#
#We've seen this before.
#
#And then we have a rather weird looking function.
#
#Calculate.
#
#That takes in any number of arguments and collects them
#
#into this value stopple.
#
#We've seen this before and if you can't remember how this
#
#works, please look at the unpacking arguments lecture.
#
#Then it also takes a mandatory key word argument parameter.
#
#So that is operator.
#
#And then what it does, is it calls the operator function
#
#with the values.
#
#That's kinda weird.
#
#How does that work? How does it know it is a function?
#
#Well, the simple answer is, it doesn't.
#
#However, because we've got these brackets after the
#
#variable name, this here must be a function,
#
#since that is the syntax for calling a function.
#
#No where calling this operator variable as a function
#
#with the values passed in as individual argument.
#
#How would we use this calculate function?
#
#You could do something like result equal calculate
#
#and then notice that calculate takes in
#
#any number of arguments.
#
#So we're gonna type twenty and four
#
#and then were gonna type operator equals
#
#the divide function.
#
#But this will pass in the divide function
#
#as the operator
#
#and then we will only call it when we reach line nine.
#
#Notice that this divide function is not called here,
#
#it is only used as a value.
#
#If you wanted to call this function,
#
#you always have to put the brackets at the end.
#
#That's how you call a function in Python.
#
#So by not putting the brackets, you are passing in the value
#
#to which this name divide refers to, which is the function,
#
#as the value for this parameter.
#
#So the operator parameter now has the same value
#
#as the divide variable.
#
#They are both this function here.
#
#So you can call it as a function, passing in the values
#
#as individual values so that will give you twenty for the
#
#dividend and four for the divisor.
#
#This here is an example of using a first-class function
#
#because you can see that you can pass it in as an argument
#
#to another function.
#
#Functions in Python are just variables that happen to be
#
#callable. You can call them with the brackets at the end.
#
#But they're no different than any other value
#
#other than that.
#
#So now you can print the result if you like,
#
#and you'll see that that has [inaudible] called
#
#the divide function. And you get 5.0.
#
#If you change this to a zero though,
#
#you will end up with trace back because you tried to
#
#divide by zero.
#
#Something important that will be a little bit of problem in
#
#this code is that the calculate function
#
#takes in any number of values.
#
#But this operator expects two values.
#
#So if you put anymore, then you will also get an error.
#
#Because now you're gonna pass in too
#
#many positional arguments.
#
#See divide takes two positional arguments
#
#but three were given.
#
#So that is a small problem with this code here.
#
#But anyway the point of it was to show you
#
#how first-class functions work.
#
#Let's do another example.
#
#I'm going to define a search function that takes in
#
#a sequence of things to search through.
#
#It will also take what you expect to find
#
#and finally it will also take a function that will be used
#
#to extract information from each item in the sequence,
#
#match it against the expected value,
#
#and see if we find what we wanted.
#
#So we will iterate over the sequence,
#
#then we will run the finder function on the element
#
#and see if it is equal to the expected value.
#
#And if it is, we will return the element
#
#otherwise we will raise a runtime error,
#
#saying something like,
#
#could not find an element with expected.
#
#So this is a little bit of a confusing function there
#
#because it uses some parameters together with
#
#other parameters to find a third parameter.
#
#So a little bit weird but lets say now we have a list of
#
#friends and we want to find out which friend is called
#
#Bob Smith. Which here doesn't doesn't exist.
#
#The first thing we have to do is we have define a function
#
#that will run on one of these dictionary's,
#
#and give us back the name.
#
#So we will say, get friend name,
#
#and we will make it take one parameter
#
#and we'll say return friend, name.
#
#So here we have a function that, if we run it on an element
#
#in this sequence, we give us back the name property
#
#of that element.
#
#Be that what it may, remember this may fail if the element
#
from operator import itemgetter

#doesn't have a name property.
#
#Then we're going to print out the search,
#
#which is this function up here.
#
#We're gonna pass in the friends as our sequence
#
#so this search function is going to iterate
#
#over our friends.
#
#Then we're going to look for, Bob Smith.
#
#And finally how we're going to extract that value
#
#from each element is going to be by the
#
#get friend name function.
#
#So just to recap, get friend name
#
#will be the finder function.
#
#So that will run on each element.
#
#For example, for the first one, it will run on this
#
#dictionary here, and it will give you back the name
#
#property of that value. So you'll get back Rolf Smith.
#
#The Rolf Smith will be here, and you'll compare it with
#
#the expected value, which is Bob Smith.
#
#If they match, you will return that element,
#
#which is this dictionary.
#
#The same thing will happen for all the other ones.
#
#At this point, we don't have our friend called Bob Smith.
#
#So by running this we will get the run-time error.
#
#Could not find an element with expected.
#
#However, if we change this to Rolf Smith,
#
#then you will get it to work.
#
#The name is Rolf Smith and the age is twenty-four.
#
#This is quite a confusing bit of code but is a prime
#
#example of how first-class functions can be useful.
#
#So I would recommend giving it a go, playing around with it,
#
#see if it makes sense. And if it doesn't please ask a
#
#question in the course Q and A.
#
#Of course we're always happy to help.
#
#This is also a great place to use a lambda function.
#
#So instead of using that function, you can just define
#
#something like this,
#
#and just created it there where it is used.
#
#This is an alternative. No one is better than the other.
#
#You can do what you prefer. The other one is slightly longer
#
#but it does have a nicer name.
#
#Because you get the function name and it tells
#
#you what it does.
#
#So that's a good thing as well.
#
#Finally, you can use neither of these,
#
#do you can not define your own function or use a
#
#lambda function.
#
#You can just use a built-in from operator,
#
#import item getter.
#
#And here instead of this lambda function that is used to get
#
#a property of a object,
#
#you can use item getter
#
#with name.
#
#And that does exactly the same thing.
#
#This here, is a function that creates a function and
#
#lets you use it afterwards.
#
#So this is a little bit more advanced. We're going to learn
#
#more about functions that create other functions later on.
#
#So there you have it, that is the same thing.
#
#I set aside the operator built-in module,
#
#in fact quite a few of
#
#the Python built-in modules are amazing and really useful.
#
#All right, that's everything for this video.
#
#I hope you've enjoyed it, I hope you've learned something,
#
#and I'll see you in the next one.
#
#0:24
#1000
#
#
#▲
#
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")

    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20,4, operator=divide) #TypeError: divide() missing 2 required positional arguments: 'dividend' and 'divisor'

print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return  elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends =  [
    {'name': 'nitin', "age": 33},
    {'name': 'Rolf Smith', "age": 33},
    {'name': 'nitin', "age": 33}
]

print(search(friends,"Rolf Smith",itemgetter("name")))