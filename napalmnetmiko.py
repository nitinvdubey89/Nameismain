# napalm can do multi vendor support
# napalm has many get apis i.e. get bgpg, get lldp neighbors, get network instances


import getpass
from napalm import get_network_driver
import json



driver = get_network_driver('ios')
output = dir(driver)
print(type(output))

for item in output:
    print('item is ' + item, end='\n')
# napalm will automatically select the correct driver or the set of functions for cisco ios

optional_args = {secret : 'cisco'}
ios = driver('10.1.1.10', 'andrei', 'cisco' , optional_args= optional_args )
ios.open()

output = ios.get_facts()
dump = json.dumps(output, sort_keys=True, indent = 4)
print(dump)

output = ios.get_arp_table()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump )


print(dir(ios))

## arp table code

output = ios.get_arp_table()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump )


output = ios.get_users()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump )
#get_arp_table returns a list of dictionaries,  each entry in arp table, there is a dictionary

## checking connectivity between devices R1 and R2

output = ios.ping(destination='10.1.1.20', count=2 , source='1.1.1.1' )
ping = json.dumps(output, sort_keys=True , indent=4)
print(ping)



## ping module


for item in output:
    print(item)

dump = json.dumps(output , sort_keys=True ,  indent=4)
# json.dumps will return a string and takes the dictioanry i.e. output as an argumetn
print(dump)

with open('arp.txt' , 'w') as f:
    f.write(dump)


ios.close()

# napalm will use netmiko incase of ios therefore it will be ssh udername and pass