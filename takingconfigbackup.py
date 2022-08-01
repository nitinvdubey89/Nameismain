import paramiko
import time
import getpass
import paramikorefractoring
from datetime import datetime ## we need to store configuration backup date and time ## datetime is a class

now = datetime.now()
print(now)
print(dir(now))
print(type(now))

#We can use dir() function to get a list containing all attributes of a module.

### /n is important after every send command so that it gets printed out
# time.sleep is required before calling the recieve buffer so that the output can be collected 

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
client=paramikorefractoring.connect(**router1)
shell=paramikorefractoring.getsh(client)

paramikorefractoring.send_command(shell, 'terminal length 0')
paramikorefractoring.send_command(shell, 'enable')
paramikorefractoring.send_command(shell, 'cisco')
paramikorefractoring.send_command(shell, 'show run')


now = datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router1["server-ip"]}_{year}--{month}-{day}.txt'
print(file_name)

#an
#f - string is a
#literal
#string, prefixed
#with 'f', which contains expressions inside braces.The expressions are replaced with their values

output = paramikorefractoring.show(shell)
print(output)

## save the output to a file but we do not want to save the send_commd outputs to the file
## remove the first and last lines of the output from the output string
## we can use the splitlines functions and then we will remove the elements from the list

output_list = output.splitlines()
print(output_list)
## we can do slicing here
output_list = output_list[11: -1]
print(output_list)

## we can write a list and not a python string to  a file
## to get string fromm a list , we can use a join method
output = '\n'.join(output_list)
#Join all items in a tuple into a string, using a hash character as separator:
#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.

#myDict = {"name": "John", "country": "Norway"}
#mySeparator = "TEST"
#nameTESTcountry
#x = mySeparator.join(myDict)
#Join all items in a dictionary into a string, using the word "TEST" as separator:
#print(x)

print(output)

with open(file_name, 'w') as f:
    f.write(output)

paramikorefractoring.close(client)

## keeping backup versions and keep one month of backups