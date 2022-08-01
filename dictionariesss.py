friend_ages = {"Rolf": 24,"Adam": 30, "Anne": 27, "Bob": 45}
print(friend_ages["Adam"])


for friends in friend_ages:
    print(friend_ages[friends], end=' ')

for friends in friend_ages:
    print(friend_ages, end=' ')

for friends in friend_ages:
    print(friend_ages, end=' ')

if "Bob" in friend_ages:
    print(f"Bob: {friend_ages['Bob']}")

friend_ages["Rolf"] = 30
print(friend_ages)

values  = friend_ages.values()
keys = friend_ages.keys()

for  VALUES, KEYS in friend_ages.items():
    print(f"{VALUES} and {KEYS}")


#List_of_dictionaries

friends = [{"name":"Rolf","age": 24},
           {"name":"Adam","age": 30 },
           {"name":"Anne","age": 27 }]

print(friends[0]["name"])


# keys must be string, integeter or any other hashable types
#So start with the question i.e. Why and how are Python functions hashable? First, one should know what
# actually hashable means in Python. So, hashable is a feature of Python objects that tells if the object
# has a hash value or not. If the object
# has a hash value then it can be used as a key for a dictionary or as an element in a set.
#An object is hashable if it has a hash value that does not change during its entire lifetime.
# Python has a built-in hash method ( __hash__() ) that can be compared to other objects.
# For comparing it needs __eq__() or __cmp__() method and if the hashable objects are equal then they have the same hash value.
# All immutable built-in objects in Python are hashable like tuples while the mutable containers
# like lists and dictionaries are not hashable.
#Objects which are instances of the user-defined class are hashable by default, they all compare unequal,
# and their hash value is their id().
#Example: Consider two tuples t1, t2 with the same values, and see the differences:

t1 = (1, 5, 6)

t2 = (1, 5, 6)

# show the id of object
print(id(t1))

print(id(t2))
#In the above example, two objects are different as for immutable types the hash value depends on the data stored not on their id.

#Example: Let’s see lambda functions are hashable or not.

# create a one-line function
l = lambda x: 1

print(l)
# show the hash value
print(hash(l))

# show the id value
print(id(l))

# show the hash value
print(l.__hash__())

#Example: Let’s see user defined def based function are hashable or not.

# create an empty function
def fun():
    pass


# print types of function
print(type(fun))

# print hash value
print(fun.__hash__())

# print hash value
print(hash(fun))

#Therefore, any user defined function is hashable as its hash value remains same during its lifetime.



