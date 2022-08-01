### configure arista and cisco with vlan and routing protocols
import getpass

from netmiko import ConnectHandler

password = getpass.getpass('Enter Arista1 password')
arista_device = {
    device_type: 'arista_eos',
    host: '192.168.0.50',
    username: 'admin',
    password: 'pass123',
    port: '22',
    secret: 'password',  ## enable scret or sudo pass
    verbose: True
}

connection = ConnectHandler(** arista_device)

if not connection.check.enable_mode():
    connection.enable()

with open('arista_config.txt') as config:
    commands = config.read().splitlines()
output = connection.send_command('show interface status')

print(output)
print(commands)

## define a file named devices.txt with following table
# cisco_ios:192.168.122.30:admin:cisco
# arista_eos:192.168.122.10:admin:arista
# arista_eos:192.168.122.20:admin:arista

with open('devices1.txt') as f:
    file_content = f.read().splitlines()
print(file_content)

devices = list()
for item in file_content:
    tmp = item.split(':')
    devices.append(tmp)


for device in devices:
    net_device  = {
        device_type: device[0],
        host: device[1],
        username: device[2],
        password: device[3],
        port: '2',
        secret: device[3],  ## enable scret or sudo pass
        verbose: True
    }

connection = ConnectHandler(**net_device)

if not connection.check_enable_mode():
    connection.enable()

config_file = input('Enter the configuration file for device type' + device[0] + 'with ip' + device[1])
print('Sending commands to device...')
with open('config_file') as config:
    commands = config.read().splitlines()


output = connection.send_config_set(commands)
print(output)
print('Disconnecting.....')
print('#'* 50)

print(devices)