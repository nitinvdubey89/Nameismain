## native data serialization module for python is called pickle
# pickle is python propeitary i.e. you can load or deserilize data only back to python
# we cannot exchnage this data between different languages

# write only take strings as input and not dictionary

## native data serialization module for python is called pickle
# pickle is python propeitary i.e. you can load or deserilize data only back to python
# we cannot exchnage this data between different languages
# non python programs will not be able to reconstruct pickled python object
# pickle is binary protocol for serialising and desrialising python objects
# it converts python objects into bytes for encoding and loads the bytes back into python objects when decoding
# besides inter-op issue it is not considered secure
# one should unpickle data that we trust , it is possible to construct malicious serialized
# data which will execute arbitrary code
# never unpickle data that we recieved from untrusted source
# safer serialization method is json  that will be appropriate if you are processing untrusted data


import pickle
friends1 = {"Dan": [20,"London", 3234342], "Maria":[25,"Madrid",43525222]}
friends2 = {"Andrei": [35,"Bucharest", 324342], "Nina":[25,"Barcelona",435222]}
friends = (friends1, friends2)


# we are opening the file in binary mode
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)
    # first argument is a python object and second argument is the file object

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)
    #fucntion will read the pickled representation of object from the file and return the reconstitued object


# if you want to serialize more objects,  you can create a tuple that contains all objects and serialize that tuple



## there is a faster alternative i.e. cPickle but it does not belong to python standard library
