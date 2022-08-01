from netmiko import Netmiko
cisco_device = {
                  device_type:'cisco_ios',
                  host :'10.1.1.10',
                  username: 'u1',
                  password: 'cisco',
                  port:'22',
                  secret: 'cisco' ,
                  verbose: True
                }
connection = ConnectHandler(**cisco_device) ## **kwargs way
print('Entering the enable mode...')
connection.enable()

commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.0', 'exit' , 'username netmiko secret cisco']
connection.send_config_set(commands)
## in order to also capture outputs , we need to capture it in a variable

output1 = connection.send_config_set(commands)
print(output1)

### if one does not like making a list of commands i.e. in commands and want to write comamnds like a string
cmd = 'ip ssh version 2; access-list 1 permit any;ip domain-name network-automation.io'
output2 = connection.send_config_set(cmd.spit(';')) ## split function will return a list

cmd = ''' ip ssh version 2 
access-list 1 permit any
ip domain-name network-automation.io
'''
output3 = connection.send_config_set(cmd.spit('\n')) ## split functino will return a list

print(connection.find_prompt())
connection.send_command('write memory')

## need to check whether the loopback internface and user dont already exist

print('closing connection ')
connection.disconnect()