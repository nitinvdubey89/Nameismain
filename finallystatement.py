#finally block is used in releasing external resources such as files or network connecitons , regardless of the use of the resources

f = open('a.txt', 'r') # file should exist firstlu

try:
    f.write('write this to the file')
except Exception as e:
    print('There was an exception:', e)
finally:
    print('This code will alwaysbe exectued')
    print('File closed' , f.closed) # f.closed will give true or false
    f.close()

print('File closed:', f.closed)
#https://docs.python.org/3/library/exceptions.html