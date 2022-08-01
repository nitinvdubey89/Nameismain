import csv
with open(r'C:\Users\Nitin\Downloads\people.csv','a') as csvfile:
    # returns a writer object , we call method named write.row and we paste a list or a tuple
    # list will be converted into columns in csv
    writer = csv.writer(csvfile)
    # writer object and csvfile is an argument
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)

with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x','x**2','x**3','x**4'])
    for x in range(1,101):
       writer.writerow([x,x**2,x**3,x**4])
    ## the above functions adds an extra new line after every row
    # to fix this problem , we add another argument named newline= ''


######### USING CSV delimiter
with open('passwd.csv', 'r') as file:
    reader = csv.reader(file, delimiter=':',lineterminator='\n')
    for row in reader:
        print(row)

####### a dialect describes the usual parameters, such as the delimiter, quoting mechanism, the escape character,
# and the line terminator

##
#print(csv.list_dialects())
#['excel', 'excel-tab', 'unix']
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
with open('items.csv', 'r') as csvfile1:
    reader=csv.reader(csvfile1,dialect='hashes')
    for row in reader:
        print(row)

with open('items.csv','a') as csvfile2:
    writer= csv.writer(csvfile2, dialect='hashes')
    writer.writerow(('spoon',3, 1.5))



