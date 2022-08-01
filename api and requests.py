# requests is not a built in function
import requests
import json
## used to make http request to web servers
# this library does not come with python

response  = requests.get('https://jsonplaceholder.typicode.com/todos')

#print(type(response))
todos = json.loads(response.text)

#print(todos)
print(type(todos))

for task in todos:
    if task['completed'] == True:
        # true should be True
        print(task)