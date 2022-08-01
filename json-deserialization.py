import json

## deserialize from json into python objects
### rt is default

with open('friends.json', 'rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)

### load deserializes from a file and loads deserializes from a json string.
json_string ="""{
    "Dan": [
        20,
        "London",
        3234342
    ],
    "Maria": [
        25,
        "Madrid",
        43525222
    ]
}"""

obj  = json.loads(json_string)
print(type(obj))
print(obj)

### json does not support all python data types

#friends = {"Dan": [20,"London", 3234342], "Maria":[25,"Madrid",43525222]}
#changing the dictionary variable of type tuple and not list

friends = {"Dan": (20,"London", 3234342), "Maria":(25,"Madrid",43525222)}

### eventhough we changed to tuple , the tuple type was changed to list in the output and it was not maintained
## also set cannot be serialized in json therefore we need to convert set to a list and then serialize the list
## if i add another key value pair and the value is of type set