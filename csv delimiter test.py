import csv

with open('items.csv') as csvfile:
     writer = csv.writer(csvfile)

csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')

    with open('items.csv','a') as csvfile2:
    writer= csv.writer(csvfile2, dialect='hashes')
    writer.writerow(('spoon',3, 1.5))   
    print(csvfile2)
