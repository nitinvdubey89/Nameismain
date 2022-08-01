#We'll start a series of lectures about decorator's this is advanced python, and I'll try to show you
#many coding examples to make it clear.
#By definition, a decorator is a high order function that takes another function, is an argument,
#and extends or decorates the behavior of the later function without explicitly modifying it.
#Also, a decorator, a function.
#OK, that was the definition, but when do we use decorator's we use case is when we have a function
#that does some simple stuff and in time we want to add more functionality or code to our function.
#The problem here is that maybe sometimes we want to call the original function without the extra features
# that have been added.
#Instead of adding new code to the original function, another approach would be to create a brand new
#function, copy paste the code of the original function and add other features in the new function.
#Though these can work, we repeat code, and that is not good.
#The Python solution to this problem is called decorator's.
#It's like an on off switch we add to our functions that activates or deactivates different things in
#our functions decorator's allow us to perform some operations before calling the function.
#And in many cases, they simplify a lot of our code.
#Let me show you a very simple example, let's suppose we develop an application that checks some sort
#of permissions or user has and based on those permissions, the application executes a task or another.
#I am declaring a dictionary called Yuzu, it could be a record from a database as well.
#The username is the key, the value, let's say, James from John Smith and another key level.
#This is the security level or the privilege level.
#And he's an admin.
#And I am declaring a decorator called user has permission, a decorator is a function that takes another
#function and returns a function.
#D.F. Yuzu has permission.
#And it has one parameter called funk.
#This is a function and inside the function is body electric for user privilege level.
#So if a user of level.
#Equals equals admin.
#So if this is an admin user, I'll return the function, return func ls return none.
#This is a decorator, it takes a function, is an argument and returns a function.
#After creating the decorator, I'm going to create a function that simply returns the part, which is
#a secret information.
#So only if the user has the admin level, the application has access to the password.
#D.F. show best return and I'll write a random string.
#And we suppose this is the password.
#Now it's time to call the decorator and we pass is argument showpiece, my underlying function, this
#is a new variable equals and I'll call the decorator user has permission and the argument is show Besse
#the function that will be decorated.
#Don't call the function, just basing its name.
#That they create their returns, a function that was assigned to the variable called my function, and
#we call the function and printout the return the value.
#So print my function and I'm calling the function.
#I am executing the script.
#And we noticed that it returned the past.
#Now let's change the user's privilege level to guest and run the program again.
#OK, there is an error.
#My function equals none, none was returned and I cannot call none, but I can add anif testing condition
#so if my function not equals none, so if it's not equal to none, I'm calling it, or else I can print
#out the message.
#For example, no access.
#I am executing the script again.
#And it pointed out no access.
#We noticed how the show passport function was decorated, its behavior was changed without modifying
#it.
#That's the power of a decorator.
#You'll see decorators in many python frameworks like Flask, which is a popular lightweight web framework.
#It uses decorator's extensively and that results in elegant and intuitive code.
#This is also one of the reasons for the recently flask.
#Huge popularity.
#This simple example is working well, batiks, not Pythonic at all, the common way to use decorator's
#is to have an inner function known as a proper function.
#The decorator will return the inner function, plus free variables.
#So correctly speaking, a decorator returns a closure.
#We had a long discussion about closures in the previous lecture.
#Let's modify the decorator like this.
#I'm going to define a new function, an inner function, D.F., rapper, user hase permeation.
#And I'll invent this code.
#The nerve function runs funk, so I am calling funk.
#And I'll return the inner or the proper function.
#This is the Pythonic way to create a decorator.
#And by the way, it's common to use the name Rotbart underline and the name of the decorator, and I
#am executing the script again.
#Now, it's not necessary to have this test here, use our has permission, always returns a function
#so I can just call the function without these tests.
#I'm writing the script.
#And it pointed out none.
#The user is not an admin user, let's make it admin and it will return the password.
#OK, in this lecture, we've talked about creating and using decorator's in the following video, I'll
#show you how to use the net or if Piscean tax, which is very common and it's in fact the python way to #use decorator's.




#In this video, we're going to start learning
#about decorators.
#Decorators are great in Python
#because they allow us to very easily modify functions.
#So let's learn more about them.
#Here we've got a user dictionary that has a username and
#an access level of guest.
#Let's say that guests can't access this function here
#get_admin_password
#which returns the password to your admin panel.
#But as you can see,
#if we print out get_admin_password
#at the moment, even though we're a guest
#we're gonna get out 1234.
#There's nothing in this function
#to prevent us from doing that.
#So, the output of this video should be
#to get this function secured so that
#people that are guests cannot get the value out.
#Now of course, the clear thing that you can do
#is to put an if statement in here.
#If the user's access level is == to admin,
#then you can print out this function.
#Otherwise, you can't.
#So this will work
#if you run that, you don't get anything,
#but of course as you know,
#get_admin_password is still un-secure
#so you can still print that out
#and it'll still work.
#Because what we've done is
#we have protected this specific call to get_admin_password,
#but we haven't protected this one.
#So, this is probably not exactly what we want to do.
#The next thing we can do
#is we can define a secure function.
#For example, secure_get_admin.
#And in this one, if the user's access level is admin
#then we can return the password 1234.
#Now, a couple of things.
#Clearly get_admin_password is still defined,
#so that is not going to work,
#but secure_get_admin does protect the password.
#Running that gives you None, first of all
#when you run secure_get_admin
#because we didn't return 1234.
#Instead, we returned None which is a default.
#Then you get 1234 the next time around.
#So of course, what you may want to do
#is delete this one entirely.
#But, that poses a small problem.
#Which is that all the functions
#where you want it to be secure,
#you're going to have to add this if statement.
#And up 'til now, that is what you would have done
#if you didn't know about decorators.
#But, a decorator will allow us to modify this function
#to secure it without having to replace
#all of our functions by its secure counterparts.
#So, we don't want to do that either.
#Instead what we could do
#is define another function, secure_function
#that takes in a function.
#We've learned about first class functions,
#so we can take it in as a function there,
#and we'll say if the user's access level is == to admin
#then we will return func.
#Otherwise we'll return none.
#And now what you may be tempted to do
#is to do something like
#get_admin_password = secure function(get_admin_password).
#So, will this work?
#Well, let's run through the code.
#We've got secure_function being called
#which takes in get_admin_password,
#and when this line runs,
#we're going to check the user's access level
#and see if it's admin.
#And if it is, we're going to return func.
#So, let's see what happens.
#Now you get an error.
#NoneType object is not callable.
#Because of course, when we ran this code
#i.e., this line here,
#the user's access level was guest not admin.
#So we didn't return func,
#we returned none which is the default.
#So get_admin_password = none.
#Then we're trying to run none as if it were a function,
#but you can't do that so you get an error.
#What you would have to do is
#make sure that your user is an admin
#before you run any of your code.
#And then it will work and you will get 1234.
#So this is a step closer to what we want,
#but alas it requires that our user be an admin
#before we secure our functions.
#Ideally we would like to do something that checks
#the user's access level when you call the function,
#not when you define it.
#So, here's what we're gonna do.
#We're still going to take in a function
#but now we're going to define another function,
#which I'm going to call secure_function.
#This one I'm gonna call make_secure.
#This one doesn't take any parameters,
#and it is the one that checks.
#And, it returns calling the original function.
#Then, here we return secure_function.
#So this is a decorator.
#What happens now, and by the way
#this should be make_secure
#What happens now is that get_admin_password,
#this function that we want to secure,
#is passed to the make_secure function.
#This one defines another function,
#and by the way, in Python you can define functions
#inside a function, so that's totally fine.
#And this function here, when called,
#will check the user's access level
#and return calling the original function
#which is get_admin_password.
#So it will return 1234 if the user's access level is admin.
#So that's this function here,
#and then we return the function itself.
#Not the function call, but the function itself.
#get_admin_password will be equal to this function.
#Which calls seemingly itself, but this is okay.
#It calls get_admin_password from up here.
#So when you call get_admin_password what you're gonna do
#is you're going to check the user's access level,
#and then you're going to return the result
#of calling the function originally,
#which will give you 1234.
#At the moment you get none, but of course if you
#set the user's access level to admin down here
#and you run it again,
#then you get 1234.
#Which is exactly what we wanted.
#So this is a simple decorator.
#This simple decorator will create a function
#and replace the original function with this secure one.
#So that you can no longer call get_admin_password
#without having the admin access level.
#Now if you wanted to add a little bit of error handling
#you can do an else here
#and you can return something like
#"No admin permissions for {user['username']}."
#and that'll give you a nicer idea of what's going on
#if you don't have admin permissions.
#That's everything for this video.
#This is a simple decorator,
#and now in the next one we're going to learn more
#about using the @ syntax for decorators
#that makes this much simpler, and much easier
#to re-use and secure multiple functions
#if that's what you want to do.
#Thanks for joining me,
#and I'll see you in the next video.


#######################################################################################


#user = {'username': 'js', 'level': 'admin'}

#def user_has_permissions(func):
#    if user['level'] == 'admin':
#        return func()
#    else:
#        return None

#def get_pass():
#    return "absas123"

#my_function = user_has_permissions(get_pass)
#if my_function != None:
#    print(my_function)
#else:
#    print('No access')


#### the common way to use decorator is use an inner function known as wrapper function


user = {'username': 'js', 'level': 'admin'}

def user_has_permissions(func):
    def wrapper_user_has_permission():
        if user['level'] == 'admin':
              return func()   #printing a function or printing a closure is different
        else:
              return None
    return wrapper_user_has_permission

def get_pass():
    return "absas123"

my_function = user_has_permissions(get_pass)
print(my_function())
#Instead of rmy_function equals  only admin of remove file and then remove file of 860, we can use another
#syntax.
#Just the line before the functions definition, the function that is decorated, so we move while we
#write it into the decorator name.
#At this moment, the function called remove file doesn't exist any more on its own, it's connected
#with the decorator.
#This is known as ETA or by syntax.
#I'm going to comment about this piece of code.
#And I'll simply call the function using its name, so remove file of a Dr..
#And I'll also write the code for exception handling.
#I'm running the script.
#And I've got permission denied because the user doesn't have the admin level.
#I changed the level to admin and I'm running the script again, and the file has been removed.
#We notice that the remove file function was decorated correctly.
#In fact, this is the same just the syntax is different, you can use whichever way you prefer.
#Just remember that when using the Itzin tax, it just released, the function of Morphy is a parameter
#of the decorator function and assigns it back to the same label called remove file.
#The line of fire equals only admin of remove file is not necessary anymore.
#Here, I don't simply call the function remove file, but the decorator function that returns it based
#on some conditions.