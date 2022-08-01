import csv

with open('devices.txt', 'r') as file:
    reader= csv.reader(file, delimiter=':', lineterminator='')
    abc = []
    for row in reader:
        abc.append(row)

    for row1 in abc:
        print(row1, end='\n')
