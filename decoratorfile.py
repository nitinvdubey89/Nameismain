user = {'username': 'js' , 'level': 'admin'}
def only_admin(func):
    def wrapper_only_admin(*args, **kwargs):
        if user['level'] == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('Permission denied') #Python raise Keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program. It is used to bring up the current exception in an exception handler so that it can be handled further up the call stac
    return  wrapper_only_admin

@only_admin
def remove_file(f=None):
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

create_user_and_group('admin1', 'sudo')
update_system()