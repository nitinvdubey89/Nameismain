from netmiko import Netmiko ## class name is  captial N
## never make a python script by the name of netmiko
## try to ping the device first
## ssh using putty using u1 aand pass cisco


connection = Netmiko(host= '10.1.1.10', port = '22', username = 'u1', password = 'cisco' , device_type= 'cisco_ios')
## if write wrong credentials , we get authentication error
output = connection.send_command('show ip interface brief')
print(output) ## netmiko removes all unnecesary commands prompts and printed out the output.
# ## terminal lenght 0 was also taken care by netmiko
## no call needed for time.sleep()

connection.disconnect()