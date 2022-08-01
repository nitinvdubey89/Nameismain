import functools

def timer(fn): # fn is the decorated funciton
    import time # unix timestamps in secondss , sstarts unix epoch 1970 and can be used anywher in the globe
    @functools.wraps(fn)
    def wrapper_timer(*args, **kwargs): ## wrapper as a name is best practises *,**kwargs is needed to decorate any function
        start_time = time.time()
        result = fn(*args,**kwargs)
        end_time = time.time()
        print("first i get executed")
        print(f'{fn.__name__} execution time:  {end_time - start_time}')
        return result
    return  wrapper_timer

@timer
def sum_of_powers(n,p):
    # n = 4 and p = 2 -> 1 + 4+ 9 + 16
    nums = [x**p for x in range(1,n+1)] ## this is list comprehension
    print("i get executed after decorator")
    print(nums)
    return sum(nums)

print(sum_of_powers(10,4))
#C:\Users\Nitin\PycharmProjects\pythonProject\day-18-start-1\venv\Scripts\python.exe C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/decoratorspeedtest.py
#Traceback (most recent call last):
#  File "C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/decoratorspeedtest.py", line 21, in <module>
#    print(sum_of_powers(100000000000,4))
#  File "C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/decoratorspeedtest.py", line 8, in wrapper_timer
#    result = fn(*args,**kwargs)
#  File "C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/decoratorspeedtest.py", line 17, in sum_of_powers
#    nums = [x**p for x in range(1,n+1)] ## this is list comprehension
#  File "C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/decoratorspeedtest.py", line 17, in <listcomp>
#    nums = [x**p for x in range(1,n+1)] ## this is list comprehension
#MemoryError ## if the value is too huge


from functools import wraps


# defining a decorator
def timer(fn):
    from time import time

    @wraps(fn)
    def wrapper_timer(*args, **kwargs):  # this is a generic decorator
        start_time = time()  # retrieving the current timestamp
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'{fn.__name__} execution time:{end_time - start_time}')
        return result

    return wrapper_timer


# decorating the function
@timer
def sum_of_powers(n, p):
    nums = [x ** p for x in range(1, n)]
    return sum(nums)


s = sum_of_powers(10, 2)
print(s)


## EXPECTED OUTPUT:

# sum_of_powers execution time:0.33020472526550293
# 333332833333500000
# sum_of_powers execution time:0.33238673210144043
# 249999500000250000000000
# sum_of_powers execution time:0.36234617233276367
# 166666166667083333333333250000000000

#What is the difference between a free variable and a non-local one?
# they are the same


