numbers = [1,2,3,4]
doubled = []
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []


for num in numbers:
    doubled.append(num*2)
print(doubled)

# list comprehensino

doubled = [num*2 for num in numbers]
print(doubled)

#for friend in friends:
#    if friend.startswith("S"):
#        starts_s.append(friend)
#print(starts_s)

starts_s = [friend for friend in friends if friend.startswith("S")] # this is a new list and its not the same ID as the start_s created by above using append

print(starts_s)

# we can check the address using the ID keyword or the "is" keyword
print(friends is starts_s)
print("friends: ", id(friends), "start_s", id(starts_s))