## problem introduced by decorators
## new problem is related to introspection
# introspection is the ability of an object to know about its own attributes at run time.
## a function knows its own name and documentation
## how to preserve the name and doctstring of our decorated function ?

import functools # preserve the name and doctstring of our decorated function

user = {'username': 'js' , 'level': 'admin'}
def only_admin(func):
    @functools.wraps(func) ## preserve the name and doctstring of our decorated function
    def wrapper_only_admin(*args, **kwargs):
        '''this is a wrapper function '''
        if user['level'] == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('Permission denied')
    return  wrapper_only_admin

@only_admin ## lets remove the decoration
def remove_file(f=None):
    '''this function removes a file'''
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f'{f} is  removed')
    else:
        print('Argument is not a file')

@only_admin
def create_user_and_group(user, group):
    print(f'This function create user {user} and group {group}')
    # code that creates the user and the group

@only_admin
def update_system():
    print(f'This function update the OS')


try:
    remove_file('abd.txt')
except PermissionError as e:
    print(e)

#create_user_and_group('admin1', 'sudo')
#update_system()

print(remove_file.__doc__) ## with decorator it gives doc string and the name of the wrapper function
print(remove_file.__name__) ## decorating a function means running a function as an argument of the ddecorator function and assigning
                            # it back to the same label called the decorated function
                            ## how to preserve the name and doctstring of our decorated function ?
                            # use @functools.wraps(func)
                            # this will preserve infomration about the origincal function
                            #

