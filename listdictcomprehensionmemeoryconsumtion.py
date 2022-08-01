#There are plenty of questions and discussion about
# memory consumption of different python data types.
# Yet few of them (if any) come to a very specific scenario.
# When you want to store LOTS of key-value data in memory,
# which data structure is more memory-efficient, a dict or a list of tuples?
#At beginning I thought dict is more powerful than list of tuples
# and that power must come with some price,
# and actually an empty dict DOES occupy more memory than
# an empty list or tuple (see In-memory size of a Python structure),
# so I thought using [(key1, value1), (key2, value2), ...]
# would be more memory-efficient than {key1: value1, key2: value2, ...}.

#Looks like I was wrong.
# Just fire up the following code snippet,
# and see the mem consumption reported by your OS.
# I am using Windows XP so that task manager tells me,
# a large dict eats up "only" 40MB Ram and 40MB VIRTURAL Ram,
# but a list of tuples eats up 60MB Ram and 60MB Virtual ram.

### its not lookup efficieny we are talking about memoery efficiency

from sys import getsizeof as g
input('ready, press ENTER')
i = 1000000
#p = [(x, x) for x in range(i)] # Will print 4,348,736 40,348,736
p = dict((x, x) for x in range(i)) # Will print 25,165,964 37,165,964
print(g(p), g(p) + sum(g(x) for x in p))
input("Check your process's memory consumption now, press ENTER to exit")

#################################
## Sets in Python
## A set is a unordered collection of immutable unique objects.
#################################

## Creating sets
set1 = set()  # empty set
# x = {}             # x is a dictionary, not a set
set2 = {'a', 1, 2, 1, 'a', 2.3, 'a'}  # => {1, 2, 2.3, 'a'} -> unique unordered collection
set3 = set('hellooo python')  # =>{'n', 'e', 'p', 't', 'o', 'h', 'l', ' ', 'y'}
set4 = set([1, 2.3, 1, 'a', 'a', 2.3, 'b', 5])  # => {1, 2.3, 5, 'a', 'b'}
# set4[0]    # TypeError: 'set' object does not support indexing
set5 = {(1, 2), 'a'}  # a set can contain immutable objects like tuples
# set6 = {[1, 2], 'a'}    # TypeError: unhashable type: 'list' -> list is mutable, not allowed in set


## Iterating over a set
some_letters = set('abcabc')
for letter in some_letters:  # prints: c a b
    print(letter, end=' ')

## in and not in operators test set membership
'a' in some_letters  # => True
'aa' in some_letters  # => False
'bb' not in some_letters  # => True

s1 = {1, 2, 3}
s2 = {3, 1, 2}
s1 == s2  # => True
s1 == s2  # => True
s1 is s2  # => False

## The assignment operator (=) create a reference to the same object
s3 = s1
s3 is s1  # => True
s3 == s1  # => True
s3.add('x')  # adds to the set
print(s1)  # => {1, 2, 3, 'x'}
s3 == s1  # => True
s3 is s1  # => True

# copy() method creats a copy of a set (not a reference to the same object)
s4 = s1.copy()
s4 is s1  # => False
s4 == s1  # => True
s4.add('z')
s4 == s1  # => False

print(s1)  # => {1, 2, 3, 'x'}
## pop() method removes and returns an arbitrary set element
item = s1.pop()
print(f'item:{item}, s1:{s1}')  # => item:1, s1:{2, 3, 'x'}

s1.discard(2)  # discards element from the set, s1 is {3, 'x'}
s1.discard(22)  # no error if the element doesn't exist
# s1.remove(1)   # KeyError if element doesn't exist
s1.clear()  # Removes all elements from this set

#################################
## Set Operations and Frozensets
#################################

set1 = {1, 2, 3}
set2 = {3, 4, 5}

## difference() returns the set of elements that  exist only in set1, but not in set2.
set1.difference(set2)  # => {1, 2}
set1 - set2  # => {1, 2}

## symetric_difference() returns the set of elements which are in either of the sets but not in both.
set1.symmetric_difference(set2)  # => {1, 2, 4, 5}
set1 ^ set2  # => {1, 2, 4, 5}

## union() returns the set of all unique elements present in all the sets.
set1.union(set2)  # => {1, 2, 3, 4, 5}
set1 | set2  # => {1, 2, 3, 4, 5}

## intersection() returns the set that contains the elements that exist in both sets
set1.intersection(set2)  # => {3}
set1 & set2  # => {3}

set1.isdisjoint(set2)  # => False
set1.issubset(set2)  # => False
set1 > set2  # => False
set1 <= set2  # => False
{1, 2} <= {1, 2, 3}  # => True

## A frozenset is an immutable set
fs1 = frozenset(set1)
print(fs1)  # => frozenset({1, 2, 3})

## All set methods that don't modify the set are available to frozensets
fs1 & set2  # => frozenset({3})


