
d = {'name': 'kevin', 'age': 34, 'gender': 'male'}

print(d['gender'])
print(d.keys())
print(d.values())
print(d.items())

for  key,values in d.items():
   print(f"\n {key}", end=' ')
   print(f"\n {values}", end=' ')


## choosing a prime number for nymber so that items are distributed properly and there are as few collisions as possible

# lets take index size as 10  , multiples of 2 and 5 will be hashed to the same bucket

# hashing is good for cryptographty

#Since encryption is two-way, the data can be decrypted so it is readable again. Hashing, on the other hand, is one-way, meaning the plaintext is scrambled into a unique digest, through the use of a salt, that cannot be decrypted.
#It requires a private key to reversible function encrypted text to plain text. In short, encryption is a two-way function that includes encryption and decryption whilst hashing is a one-way function that changes a plain text to a unique digest that is irreversible.
#er: Encryption is a two-way function; what is encrypted can be decrypted with the proper key. Hashing, however, is a one-way function that scrambles plain text to produce a unique message digest.
#In simple terms, a hash function maps a significant number or string to a small integer that can be used as the index in the hash table.
...
#This article focuses on discussing different hash functions:
#Division Method.
#Mid Square Method.
#Folding Method.
#Multiplication Method.

#What does enumerate do in Python? The enumerate function in Python converts a data collection object into an enumerate object. Enumerate returns an object that contains a counter as a key for each value within an object, making items within the collection easier to access
