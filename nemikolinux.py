import time

from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
## logging communication  between netmiko and ssh deamon and all the complexities that netmiko handles

# systemctl status ssh

device = {
    device_type: 'linux',
    host: '192.168.0.50',
    username: 'u1',
    password: 'pass123',
    port: '22',
    secret: 'pass123',  ## enable scret or sudo pass
    verbose: True
}

connection = ConnectHandler(**linux)
# in linux all administrative tasks  must be done by root example : service, install a new program, create a new user or change config

## sudo /etc/shadow

##  you can use sudo su

## apt update && apt install -y apache2
# -y option will assume as answer to all prompts to run non-interactively
## dpkg  dpkg is a tool to install, build, remove and manage Debian packages.
# The primary and more user-friendly front-end for dpkg is aptitude(1).

# execute dpkg to check the status of apache2 to confirm whether its running or not
# dpkg --get-selections | grep apache2

connection.enable() ## we become root using this command the same way as we become enable in cisco , equivalent to sudo su
output = connection.send_command('apt update && apt install -y apache2')  ## this requries active internet connectino

## lets use write and read channel method instead of send commadn

connection.write_channel('show version\n')
time.sleep(2)
output = connection.read_channel()
print(output)

#A shadow password file, also known as /etc/shadow,
# is a system file in Linux that stores encrypted user passwords and is accessible only to the
# root user, preventing unauthorized users or malicious actors from breaking into the system.


####### INORDER TO TROUBLESHOOT NETMIKO , WE NEED TO START THE LOGGING PROCESS
