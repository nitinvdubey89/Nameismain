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

print('sending commands from file')
output = connection.send_config_from_file('ospf.txt')
print(output)

## debug ip ospf events and terminal monitor to view debug in ssh conection  can be used

print('closing connection ')
connection.disconnect()

## configuring using multiple configuration files 