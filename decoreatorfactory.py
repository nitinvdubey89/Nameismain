class Book:
    TYPES = ("HARDCOVER", "PAPERBACK")

    def __init__(self, name , book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name} , {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        #return Book(name, Book.TYPES[0], page_weight + 100)
         return cls(name, Book.TYPES[0], page_weight + 100)
    @classmethod
    def paperback(cls, name, page_weight):
        #return Book(name, Book.TYPES[1], page_weight)
        return Book(name, Book.TYPES[1], page_weight)

book  = Book.hardcover("HARRY POTTER", 1500)
light = Book.paperback("Python 101", 6000 )
print(book)
print(light)
book = Book("harry potter", "hardcover", 1500)
print(book)

#Class methods are used often as factories
#and I'm going to show you what that is in a second.
#And finally, static_methods are used to just place a method
#inside a class.
#Because you feel like it belongs there for some reason.
#For you as a developer, you wanna put that method in there
#because it makes sense logically for code organisation
#or something like that, then you can use that.
#I'll say though that most of the time,
#you'll be using class methods and instance methods.
#You won't be using static methods all that much.
#Let's start with our factory example
#that is going to show you how you might use a class method.
#This example is gonna be a little bit tricky
#so please bear with me for a second
#while I explain first what I've done here.
#In a class, as well as methods,
#you can also put variables
#and these become class properties.
#If you wanted to print out this tuple here,
#all you have to do is access the TYPES tuple
#inside the Book class.
#You would do Book.TYPES,
#and that is how you access this tuple there.
#You can print it out
#and you can see that you get hardcover and paperback.
#We have some data stored inside the class,
#which is this tuple here,
#and a reason why you might put some data inside a class,
#as opposed to putting it outside the class,
#is because you feel like it belongs there
#or only the Book class is going to use it,
#or maybe there is some sort of reason,
#logical reason to put that data in there.
#Here I'm creating a class that talks about Books.
#So, it makes sense to have book types inside there.
#Then we're going to create an init method for this class.
#Remember, because this is an instance method
#it creates an instance and gives it back to you,
#you need the self parameter there.
#You can call self whatever you want, once again,
#but the convention in Python is to call it self.
#And then we're going to be creating objects
#of type Book that have three things.
#A name, a book type, and a weight.
#So, we will do self.name = name,
#Self.book_type = book_type,
#and self.weight = weight.
#This is a very common thing in Python
#to create an object with three different values
#that you then store each one inside a property
#of the object itself.
#Just to recap, if you were to create a variable
#such as Book, and make it an object,
#then you will need to pass in some information,
#let's say, "Harry Potter", "hardcover", and 1500,
#then you can print book.name
#and what that's going to do is it's going
#to pass in "Harry Potter" as the value for this parameter.
#Then that is going to be assigned to the name property
#of the self object, which is essentially
#an empty container at this stage,
#and then we're going to print it out down here.
#So if we press play,
#you'll see that "Harry Potter" comes out.
#That's how the data is flowing through
#this system at this stage.
#Then I'm also going to create a repr method
#so that it's a little bit easier
#to work with these books.
#And we are going to return a Book with this name.
#It is this Book type
#and it's weighing {self.weight}g>.
#This is a representation of the book that would allow us,
#with all the data included inside,
#to recreate a book object if we wanted to.
#Remember, that is the purpose of the repr method.
#If you wanted to just print the book out nicely
#for users to read,
#then you could use the str method instead.
#Now instead of putting in book.name,
#we're just going to print book and I will press play
#and show you what the output is.
#Here's the book, "Harry Potter."
#It's a hardcover, weighing 1500 grammes.
#Now we come into the factories.
#Here's where we're gonna use class_methods.
#I wanna avoid, when I'm creating a new book object,
#when I'm calling the init method,
#
#I want to avoid passing in this "hardcover" string
#
#because I only want to be able to create books
#
#that are either hardcover or paperback,
#
#I wanna make sure that when I create a book,
#
#I use one of these two types.
#
#Right now, I can pass in comic book if I wanted to here
#
#and that would be totally fine because again,
#
#the data, this string here, becomes the value of book_type.
#
#Book_type gets assigned to self.book_type,
#
#and that gets used down here.
#
#There is no check for this,
#
#nothing is using this at the moment.
#
#What I'm going to do is I'm going to create a method
#
#that will take in the name and the weight
#
#and will create a new book object of type hardcover.
#
#I'm going to call this @classmethod hardcover,
#
#and again, because it is a class method,
#
#it takes in the class as the first parameter,
#
#usually called that cls in Python.
#
#And that is going to take in the name
#
#and the page weight,
#
#and what it's going to do is it is going to return a book
#
#with the name as the first argument,
#
#which then goes into the init method.
#
#Book.TYPES[0] as the second argument.
#
#Remember, Book.TYPES gives us this tuple.
#
#Book.TYPES[0] gives us the hardcover.
#
#And finally, the page_weight + 100
#
#for the weight of the book.
#
#I'm adding 100 because it's a hardcover
#
#so it's probably going to be a little heavier
#
#than a paperback.
#
#Hopefully this makes sense.
#
#It is a little bit confusing because you are using
#
#the class inside a method defined inside the class.
#
#Which I know is a little bit weird,
#
#but that is how you can create a new object
#
#inside of a class.
#
#This is something you can totally do.
#
#And because it is a class method,
#
#you no longer need to create your own object first.
#
#All you have to do now is say,
#
#Book.hardcover and pass in here "Harry Potter"
#
#and the page weight which was 1500.
#
#Notice that this hardcover method takes in the name
#
#and the page weight but it does not take in a type.
#
#The type is added inside the method,
#
#you don't have to pass it in as an argument.
#
#If I save and run that,
#
#you can see that now you get a book "Harry Potter,"
#
#which is a hardcover, and weighs 1600 grammes.
#
#Let's do the same thing for the paperback.
#
#Only now instead of Book.TYPES[0],
#
#I'm going to do Book.TYPES[1]
#
#and I'm going to remove this + 100.
#
#So now, if we wanted to create a softcover book,
#
#or a paperback, you can say something like,
#
#light = Book.paperback("Python 101"),
#
#and you can say for example, 600.
#
#If you then print the light book as well,
#
#you'll see that you get two books printed out now.
#
#Book "Harry Potter," which is hardcover, weighing 1600 grammes
#
#and Book "Python 101," which is a paperback,
#
#weighing 600 grammes.
#
#This is a very, very common way of using class methods
#
#because you have access to the class itself
#
#inside the method, that means that it is a perfect place
#
#to be creating new objects by using that class.
#
#With that said though, notice that I'm using Book here
#
#and I'm not using cls anywhere.
#
#Book is the class as we saw earlier on.
#
#And cls is also the class.
#
#They are interchangeable.
#
#Instead of Book, you can put cls in there.
#
#And instead of Book down here, you can put cls in there.
#
#You should do that.
#
#Use cls instead of Book and that will come in handy
#
#when you look at inheritance,
#
#which we will look at later on.
#
#Just because using cls gives you a little bit more
#
#flexibility down the line.
#
#Do use cls there since you've got access to it
#
#and if you were creating a static method
#
#instead of a class method,
#
#you would have to use book class
#
#because you wouldn't have cls.
#
#If you want to use cls use a class method,
#
#use the paramter, and you can create new objects
#
#and return them or use them however you like.
#
#Hopefully this makes sense.
#
#I know that it's a little bit confusing
#
#looking at class methods and static methods
#
#and it's been a bit of a long video
#
#but hopefully it was helpful.
#
#Hope you enjoyed it and I'll see you in the next one.


Hi, guys, and welcome back.

In this video, we're going to learn

about decorators with parameters.

Now, this is slightly different than the last video

where we looked at decorating functions with parameters,

now we're going to add parameters

to the decorators themselves.

Let's get started.

Here, we have our make_secure decorator.

And now, we are looking at two different functions.

One get_admin_password that is decorated,

and get_dashboard_password, which is also decorated.

But now, I want the get_admin_password

function to only be accessible by admins

and the get_dashboard_password to only

be accessible by users.

So if you're a guest, you will get access to neither,

but if you're a user, you'll get access to this one.

And if you're an admin, you'll get access to this one.

So how do we do this?

Well, we have a make_secure decorator here,

and notice that when this gets called,

what happens is the make_secure decorator

gets applied to get_admin_password.

But there are no brackets after this make_secure.

Now, what we're going to do is we're going to create

a function that will return the decorator,

but it will allow us to check for the access level.

Now, here's that's gonna go.

It's a little bit complicated.

We're going to create another decorator,

and this one is going to take in an access_level.

The rest of all of this is going to go inside that.

And this one here is going to return make_secure.

So we have added a third level of function,

and I know this is quite confusing,

but now what we've got is not really a decorator.

Now, I'm going to actually change the name

of these functions because the outer function,

it's not really a decorator anymore.

This one here is a decorator now.

This one is a factory, essentially,

a function that is used to create a decorator.

But what we have is a function call,

that we give it an access_level,

and then it creates a decorator and returns it.

So now we have to put the brackets in here.

And the order is very important.

The function call happens first,

and then the result is applied as a decorator.

So the function call happens first.

This will run in its entirety.

We will define the decorator function,

and we will return it.

Oh, sorry, this should be decorator there,

because we wanna return that function.

So this will run and return the decorator,

and that is the result of calling make_secure,

and then we will apply that decorator into this function.

At the end of the day, the result is the same,

but now we can pass in something like admin in there,

and something like guest in there.

Notice that because this factory does take in a argument,

you need to put the argument and the brackets in there.

The benefit of that is now inside here,

we can check that access level.

So we can say that if the user's access level

is equal to the access level that we want to secure for,

then we have access to the function.

Otherwise, we can say that this user

has no access level permissions, or for that.

So there are no access level permissions for that user.

Now if we want to run these functions, we can do.

Here I've got the get_admin_password

and get_dashboard_password.

We should get no access for either of those.

And then I'm going to change the user to an admin

and run them again, and now we should allow this one,

but not that one.

Let me save that and run it,

and you'll see that you get that problem exactly.

Indeed, we actually have access to the user dashboard there.

We wanna change that, make sure that's for users only

since that was the original intention.

Let's run that again.

And you get no admin permissions for Jose,

no user permissions for Jose.

But Anna does have admin permissions,

but no user permissions.

something that you may wanna look into

to improve this further is, instead of using strings

for your access levels, you can use integers.

So guest can be zero, user can be one,

and admin can be two.

And then, instead of checking a quality here,

you can actually do greater than.

And that'll let admins access the user passwords

as well, if you want that.

That's it for this video.

I wanted to show you how to create decorators

that have parameters.

And I know that they are a bit confusing.

There are three levels of functions,

which make these the most complicated Python code

that you'll see in most Python courses,

and certainly throughout your programming, as well.

But hope you've learned something.

Hope you've enjoyed it.

And I'll see you in the next video.