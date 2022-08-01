def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1,3,5))
# if you multiply 1 with a tuple then the answer is a typle


def add(x,y):
    return x + y

nums = {"x": 4, "y":7}
print(add(**nums))

def apply(*args,operators):
    if operators == "*":
        return multiply(args) # the stateme is passing args as a tuple  there we need to change this to *args
     # * will unpack the variables otherwise , nested action will not work
    elif operators == "+":
        return  sum(*args)
    else:
        "No valid operator provided to apply()"

print(apply(1,3,6,7, operators="*")) # the 1,3,5,7 is taken as tuple