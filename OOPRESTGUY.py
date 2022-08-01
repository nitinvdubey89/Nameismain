'''Hi guys and welcome back.

#In this video we're gonna talk about

#object oriented programming.

Object oriented programming is a bit confusing

when you get started, so if you've never seen

#object oriented programming before, just take it easy

#with the next few videos, watch them a couple of times

if you need to, ask any questions in the course

of the Q and A, if necessary we'll be there to help you out.

Object oriented programming allows us as developers

to write code in a slightly different way

than we would write if we didn't have

object oriented programming.

The purpose of object oriented programming

is to make our life as developers simpler

by allowing us to write code that looks like

what we would work with in the real world

if we were talking about, you know,

real world things like chairs and tables

and printers and things like that,

as opposed to code and data passing

from one function to another.

So that is the purpose of object oriented programming.

And in this video we're going to look at how

it works in Python.

Let's say that you've got a dictionary like this one here

which shows some information about a student.

Now clearly this thing here is not a student,

it is a dictionary that has some data.

And as we know, programming is all about data,

passing data from one place to another and so forth.

So what we've got here is some data that is probably

about a student somewhere in our classroom

or something like that.

Then we've got a function that takes in a sequence

and adds the entire sequence together and divides it

by the length of the sequence and then returns that.

So it gives you the average of a sequence.

For example we could use it to calculate the average

grade of Rolf.

How would you do that?

Well you would have to use the function

and give to it Rolf's grades.

So you do average student grades, like that.

So if we run that you'll see that we get out

the value 88.0 which is the average grade.

However, there is something about this function

which is very important when you are thinking

about object oriented programming,

which is that this function doesn't know anything

about the student.

The function only operates on the input that it receives

and that could be a set of student grades

or it could be something else.

So when we as developers are talking specifically

about a student and we want to calculate specifically

the average student grade for Rolf, it is much nicer

if we can say hey student, what's your average

as opposed to get the average of this sequence

that could or could not be related to the student.

So basically what I want to do is student.average.

This is what object oriented programming

will allow us to do.

But in order to do that, student cannot be a dictionary

because dictionaries you can't do that on.

You have to code your own thing in Python that will

allow you to call the average method inside it,

and that will give you the average of the student.

So it is a very different approach,

and it is not necessarily superior,

but it is different and allows

you to think of your programmes in a different way.

So let's rewrite this example here using object

oriented programming so you'll have a look at the syntax.

The syntax for object oriented programming

or to define a class in Python is to type out a keyword

class, and then the name of your class.

So a class is a definition of something,

but it doesn't create a particular student here,

we're only defining how a student will behave.

So you can say inside the function,

notice that there are four spaces of indentation,

you can define functions.

So you can define a special function called

the underscore underscore init underscore underscore.

So this function name is very important,

and it has two underscores at the start

and two at the end.

And then you put your brackets and in here we're going

to type out self.

Although this is again just a variable name

like in every other function and you can call it

whatever you want, it doesn't have to be self

if you don't want, but self is the convention in Python.

Then in the body of the function you can define

anything you want.

For example, self.name is going to be Rolf.

And what this is doing is it is taking whatever self is

and it is accessing the name property inside of self.

So here we're using the dot notation

to access something inside of self,

and what we're accessing is the name property.

And then we're giving it a value of Rolf.

What that means is that when we use this class

to create something, that thing is going

to have a name of Rolf.

So here's how you create a thing from a class.

We can say something like student, notice that now

this is lowercase because this is a new variable

that we're creating right now,

is a student, which is uppercase S because this the class.

And now we're going to tell it to use the class

to create what's called an object in Python

to create a new thing that behaves

like what this class defines.

So when you do this Python creates a new

essentially empty container if you will

and it runs the init method.

By the way it is a method and not a function

because it is inside of a class.

So when a function is inside of a class

it's called a method.

So when you call the student class,

notice that this bracket notation here

is used to call a function normally.

But we can also use it to call a class.

When you call that Python will automatically

call the init method for you and it will create

this empty thing called self, and you will be able

to modify the name property inside self

and give it the value Rolf.

The name property won't exist by default so doing

this also creates it, which is quite nice.

So once that's done and this self object contains

a name property, Python will give you back that self.

And student will become a name

for the self thing we created,

that thing being an object, that's what they're called.

So we're using this class through the init method

to create an object and assign the name property

inside that object to the string Rolf.

Then that object is what becomes the value

for our student variable.

So you can now do print student.name,

and here what we're doing is we're accessing

the name property of our student variable

which as you know is the self

that we created earlier on, so that will give you Rolf.

And if I run that you see that Rolf comes out.

This is how object oriented programming works in Python.

You call a class, the init method runs,

and what you get back is the object you created

and in the init method you have the opportunity

to set and change its properties.

So what we've got here is the name property

that we're changing.

As well as self.name equals Rolf, we can do self.grades

and make it equal to what we had before,

something like that.

So we're making the grades property of self

equal to this tuple.

And then when the function finishes,

the class gives back self to student

and now you can print out student.grades

if you want and that property will exist there as well,

as you can see.

So nothing terribly complicated up til now.

There's a bit of data being passed from

one place to another,

but this is no different to what we had before really.

If you wanted to get the average of these grades

you would still have to pass them to a function

called average for example and that would give you

the average if you had the function defined.

But using object oriented programming,

there's one more thing you can do which is going

to simplify your life greatly, and that is the main

point of object oriented programming,

which is to define another method such as

the average method inside the class.

And this method will take self as a parameter.

Notice that self again doesn't have to be self,

you can call it whatever you want.

That's just the convention in Python,

we usually call it self but you can call it

whatever you want.

So if you define a method inside a class,

all the methods inside the class have to take a parameter

which will be the object that was created initially.

You can do return sum of self.grades divided by len

of self.grades.

Notice how this method here does not take a sequence,

it just uses the object that was created up here.

So how does Python know that it needs to call

this method with this data here.

Well here's how it works internally.

When you create a new class, the init method

runs and you get this new object placed in student.

Then whenever you want to call this method here,

all you have to do is type out student, the class,

dot average, and then of course because this is essentially

another function, you put in there the student object.

And what this is doing is it's hauling the average method

inside, that's what the dot means,

inside the student class,

so that's this one there.

And the self parameter is going to take the value

of the student variable which has that object

that was created earlier on that contains

the name and the grades.

So if we save that and run it,

you can see that you get 88.2.

Now this is a little bit verbose, there's a few

too many words in there, so Python has a nice bit

of syntax that you can use instead of this one

which is to remove the student argument

from the average function and instead of calling

the average method inside the class,

call it on the object itself.

So if you do student.average, Python is going

to realise that student is a student object,

so you probably want to pass it as self,

as the first argument.

So it will do the conversion for you,

that is the same thing and one is the other,

but this is a little bit shorter,

a little bit easier to read.

And if you name your variables well,

then this is pretty obvious what it's gonna give you back,

it's gonna give you the average of this student.

Now you can make it even better, type average grade say,

and that's going to be just a little bit

more readable as well.

And just to show you that this works,

it does exactly the same thing.

So this is the key benefit of object oriented programming.

You can define methods inside a class

that use the object that was initially created

by the init method within them.

Show that and you don't have to keep track

of multiple different pieces of data

and the object itself can contain these methods

that you want to use inside it,

so all the data and the methods are in one place

inside the class.

Now the init method can also take arguments

or have parameters.

For example, we can have a name parameter as well as self,

so just to recap, all methods inside a class

need to have a parameter such as self

so they can take in the object that

you have been constructing.

But they can also take more arguments,

so here we're going to have another parameter,

the name parameter, and then you'll put the value

of that parameter in the bracket

of the student class call.

So we can put here Bob, let's say.

So now Bob will become the value for name.

Notice that self is given for you, so you don't have

to give it a name, this here will become

the value for name.

But notice that we're not using this name parameter anyway.

We are accessing here self.name, but that's the name

property inside self, it is not this parameter.

If you wanted to access this parameter,

you can do that by doing something like that.

Self.name which is the name property inside self

will take the value of the name variable

inside this method which is this parameter here.

So now if you print student.name you'll see that Bob

will come out because that is what we defined

in the init method.

Let's do the same with grades.

And now as well as name, we have to pass in

a set of grades for the student.

For example, we will do this one,

give it just a little bit of a different set

of grades there, and now we can press play

and notice how the average grade changes.

The average grade is now being calculated

from this set of grades because they are stored

in self.grades for this student.

So when the average grade method is called

it uses those grades.

Remember that you can define multiple students if you want

and that's totally fine.

This call here in line 10 will call the init method,

it will give you a new object, it will populate

self.name of that object with the name argument

and self.grades of the self object with this argument.

And it will give you this student variable back.

I'm gonna call this student two.

The student two variable, exactly the same thing,

calls the init method, passes Rolf as the name

and it creates a new object and sets the name

property of that new object to Rolf

and the grades property of that new object

to this set of grades here.

And what you end up with are two separate

containers of data.

The student variable which is Bob and has these grades,

and the student two variable which is Rolf

and has these grades.

So when you call student2.average_grade,

again what Python is doing is it's calling the student class

and passing student to there.

So self is student two.

When you sum the grades you're going to be summing

these grades here because those are the grades

that are stored inside student two.

But of course you can still do student2.average_grade

instead as that is a bit simpler.

Pressing play now will give you 92.2 and 88.2

as the two averages, one for each student.

All right, that's everything for this video.

I wanted to tell you a little bit about

how object oriented programming works in Python,

how you can define classes, how objects are created,

and how methods work so that you can call them

with the data in those objects.

I hope it's all clear, but if it isn't,

please ask a question in the course Q and A,

we'll be more than happy to help you out.

Thanks for joining me in this video

and I'll see you in the next one.'''