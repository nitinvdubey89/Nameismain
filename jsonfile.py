#JSON java script object notation and is a light weight data interchange format
# it is easy for humans to read and write and for machines to parse and generate
#json has become the de facto standard for information exchange
# perhaps you are gathering information through an API or storing your data from python in a database like mongodb
# we go with json if we inter-operability outside the python eco system or we want a text format to store data
#json is more secure, deserialization of untrusted json does not create an arbitrary code executtion vulnerabilty
#json is preferrable over pickle ,
# however there is major drawback, json can only represent a subset of python builtin types
# an no custom classes, pickle can represent an extremely large number of python types
# you use pickle when you are not interested in inter-operabillity and security is not of concern
# you use json when we need inter-op between application and security concerns and
# we are not interested in preserving every python data pipe


import json  # native module
#friends = {"Dan": [20,"London", 3234342], "Maria":[25,"Madrid",43525222]}
friends = {"Dan": (20,"London", 3234342), "Maria":(25,"Madrid",43525222)} #, 4: {1,2}}
# if we add a set in the end then the json will fail , either use pickle or convert the set to  a list i.e. list({1,2})

print(type(friends["Dan"]))

# json module has two functions for serialising python objects into json format
# dump which saves the data to file on disk
# dump as which takes a python object and returns json encoded string

with open('friends.json' , 'w') as f:
    json.dump(friends, f ,  indent=4)
    # the output is a file with string representation of the dictionary

# sometimes we just want string representation of python object  in json format
# dumps takes in the python object and returns jspn encoded string
json_string = json.dumps(friends)
print(json_string)
print(type(json_string))


json_string1 = json.dumps(friends, indent=4)
print(json_string1)
print(type(json_string1))

### json is meant to be easily readable by humans , imagine what would json string look like if we serialize tons of information nand not very readable
## indent controls the indentation size of nested structures
