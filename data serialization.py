friends = {"Dan": [20,"London", 3234342], "Maria":[25,"Madrid",43525222]}

with open('friends.txt', 'w') as f:
    f.write(friends)

# write only take strings as input and not dictionary

## native data serialization module for python is called pickle
# pickle is python propeitary i.e. you can load or deserilize data only back to python
# we cannot exchnage this data between different languages
#non python programs will not be able to reconstruct pickled python object
# pickle is binary protocol for serialising and desrialising python objects
# it converts python objects into bytes for encoding and loads the bytes back into python objects when decoding
# besides inter-op issue it is not considered secure
# one should unpickle data that we trust , it is possible to construct malicious serialized data which will execute arbitrary code
# never unpickle data that we recieved from untrusted source
# safer serialization method is json  that will be appropriate if you are processing untrusted data
