from user import User
from werkzeug import security
from werkzeug.security import safe_str_cmp

users = [
    User(1,'nitin','asdf')
   # {
     #   id: 1,
    #    "usersname": 'nitin',
    #    "password": 'asdf'
    #}
]
username_mapping =  { u.username:  u for u in users} # this is a set comprehension
userid_mapping = {u.id: u for u in users}

    #'nitin': {
   # 'id':1,
    #'username': 'nitin',
    #'password': 'asdf'

#}#}

#userid_mapping = {1: {
#    'id':1,
#    'username': 'nitin',
#    'password': 'asdf'

#}}

def authenticate(username,password):
    #user = userid_mapping.get(username, None) #get function is another way of getting the dictionary keyway
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user
    #if user and safe_str_cmp(user.password, password): # usually its not good to compare string like this because can be a problem
        # with encoding , string encoding utf-8 , ascii, unicode
        # safe_str_cmp works on all python version and all systems safer way to compare strings
     #   return user

def identity(payload): # payload is the content of JWT toke
    user_id =  payload['identity']
    return User.find_by_id(user_id)