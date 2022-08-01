
user = {'username': 'js' , 'level': 'admin'}

def only_admin(func):
    def wrapper_only_admin(*args, **kwargs): ## this *args and **kwargs means i can call any func or any positional keyword argument
        if user['level'] == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('Permission denied')
    return  wrapper_only_admin # not calling the funciton but just returning it


## just a line before functions definition , remove file is the decorated function
@only_admin ## at this point the function remove_file does not exist anymore on its own and its connected with the decorator.
            # this known as at or pie syntax
def remove_file(f=None):
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f'{f} is  removed')
    else:
        print('Argument is not a file')

#raise PermissionError('Permission denied')
#PermissionError: Permission denied

#The exception is raised becasue i can see that permission is denied , we can catch this exception


## afer i add the decorator function i.e @ or pie i will comment out the try catch
#try:
#    remove_file = only_admin(remove_file)
#    print(type(remove_file))
#    remove_file('abd.txt')
#except PermissionError as e:
#       print(e)
#       print(type(e))

#remove_file = only_admin(remove_file)

try:
    remove_file('abd.txt')
except PermissionError as e:
    print(e)

