import requests
import json


########## serialization of object in pickle or json
def serialize(obj, file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    elif type == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj,f)
    else:
        print('Invalid serialization.Use pickle or json!')

######### deserialization of object in pickle  or json

def deserialization(file, type):
    if file == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            obj == pickle.load(f)
    elif type == 'json':
        import json
        with open(file, 'r') as f:
            obj = json.load(f)
            return obj
    else:
        print('Invalid serialization. Use pickle or json!')

if __name__ == "__main__":

#if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}

    # serialize using pickle
    serialize(d1,'a.dat','pickle')

   # Deserialization
    myDict= deserialization('a.dat','pickle')
    print(f'pickle: {myDict}')

    print('#'*20)

   #serialization using json
    serialize(d1,'a.json','json')

   #deserialization
    x = deserialization('a.json','json')
   # Notice how the tuple value was not preserved!
    print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}



