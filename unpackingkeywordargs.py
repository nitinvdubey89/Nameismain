import pprint

def named(**kwargs):
    print(kwargs) # this retruns a dictioary , keyword gets colllectee and built into a dictioanry

def name(name, age):
    print(name, age)
named(name="Bob",age  =25 )

details  = {"name": "Bob", "age": 25}
name(details,25)
name(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")

print_nicely(name ="Bob", age=25)

##
#def post(url, data = None, json = None, **kwargs):
#    return  request('post', url , data = data , json = json , **kwargs)
###
