import requests
import json
import csv

## write.row is  the main function
# response.text is the main variable to load in json

response = requests.get('https://jsonplaceholder.typicode.com/users')
### always rememeber to use response.text otherwise we will only see 200 in response

mylist = json.loads(response.text)
print(mylist)
#print(type(mydict))

with  open('new.csv', 'w') as csvfile4:
        writer = csv.writer(csvfile4)
        writer.writerow(('name','city','GPS co-ordinates','Company name'))
        for items in mylist:
         writer.writerow((items['name'],items['address']['city'],items['address']['geo'],items['company']))
            ## accessing nested list

with open('new.csv', 'r') as csvfile1:
    reader=csv.reader(csvfile1)
    for row in reader:
        print(row)


# with open('items.csv', 'a') as csvfile2:
#            writer = csv.writer(csvfile2, dialect='hashes')
#            writer.writerow(('spoon', 3, 1.5))


############# ALTERNATE SOLUTION FROM UDEMY TEACHER ###################

###################
# Coding Challenge Solution
###################

import json
import requests
import csv

# getting the json data from the server
response = requests.get("https://jsonplaceholder.typicode.com/users")

# loading the json encoded string into a Python Object
# users it's a list of dictionaries
users = json.loads(response.text)

# opening the csv file for writing
with open('users.csv', 'w') as f:
    writer = csv.writer(f)

    # write a header to file
    writer.writerow(("Name", "City", "GPS", "Company"))

    # iterating over the users list
    for user in users:
        # getting the data from the dictionary
        name = user['name']
        city = user['address']['city']
        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']
        # constructing the GPS coordinates in form of (lat, lng)
        geo = f'({lat},{lng})'
        #In Python source code, an f-string is a literal string, prefixed with f ,
        # which contains expressions inside braces. The expressions are replaced with their values.” (Source)

        company_name = user['company']['name']

        # writing to csv file
        csv_data = (name, city, geo, company_name)
        writer.writerow(csv_data)

### The resulting CSV File (users.csv):
# Leanne Graham,Gwenborough,"(-37.3159,-37.3159)",Romaguera-Crona
# Ervin Howell,Wisokyburgh,"(-43.9509,-43.9509)",Deckow-Crist
# Clementine Bauch,McKenziehaven,"(-68.6102,-68.6102)",Romaguera-Jacobson
# Patricia Lebsack,South Elvis,"(29.4572,29.4572)",Robel-Corkery
# Chelsey Dietrich,Roscoeview,"(-31.8129,-31.8129)",Keebler LLC
# Mrs. Dennis Schulist,South Christy,"(-71.4197,-71.4197)",Considine-Lockman
# Kurtis Weissnat,Howemouth,"(24.8918,24.8918)",Johns Group
# Nicholas Runolfsdottir V,Aliyaview,"(-14.3990,-14.3990)",Abernathy Group
# Glenna Reichert,Bartholomebury,"(24.6463,24.6463)",Yost and Sons
# Clementina DuBuque,Lebsackbury,"(-38.2386,-38.2386)",Hoeger LLC