a = lambda x , y: x+y
b = a(5,7)
print(a(5,7))
print(type(b))

(lambda x , y: x+y)(5,7)

# not very frequently used but below are some use case

def double(x):
    return x*2
sequence = [1,2,3,4,9]
doubled = [x*2 for x in sequence]

print(doubled)
#Interpreter translates just one statement of the program at a time into machine code. Compiler scans the entire program and translates the whole of it into machine code at once. An interpreter takes very less time to analyze the source code. However, the overall time to execute the process is much slower

double1 = map(double, sequence) # applied double function to seqence

double2 = list(map(lambda x:x*2,sequence))
print(double2)