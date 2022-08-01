friend_ages = {"Rolf": 24,"Adam": 30, "Anne": 27, "Bob": 45}

ravi = [1,2,3,4]
rahul = (('Bob',42,'Mechanic'), ('kumar',42,'Mechanic'))

print(rahul[0])

#for t,u in rahul: # this does not work
#     print(t,u) # this does not work

head, *tail = [1,2,3,4,5]
print(head)
print(tail)

t, u = rahul
print(t,u)


print(list(friend_ages.items()))
print(type(friend_ages.items()))
print(friend_ages.items())


for t in friend_ages.items():
    print(t , end=" lalalala ")


for ravi,_ in friend_ages.items():
    print(ravi)
#for ravi, in friend_ages.items():
#ValueError: too many values to unpack (expected 1)
# use _ to ignore

x = (5,11)
print(x)

y =  5, 11
print(y)
print(type(y))

a, b = 5, 11
print(a)
print(b)

c, d = y
print(f"{c} {d}")

