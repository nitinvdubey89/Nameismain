# paramiko is a python implementation of ssh protocol
# paramiko uses C programming language to obtain the highest performance for low level crytographic concepts
# SSH is the most commonly used for remote management of networking devices and servers
#  nornir, netmiko and paramiko, paramiko is usually the tool of choice
# paramiko needs to be installed before using
#  if  we are using pytcharm and venv which is different from the main python installation then thats not enough
# we have to install paramiko in the virtual environment too
# to test whether paramiko is in venv or not


## enable ssh on the cisco router , we can first telnet and se
# hostname R1
# ip domain-name domain.com
# crypto key generate rsa
# choose key lenght of 2048
# ip ssh version 2 ==> this opens port 22
# line vty 0 4
## transport input ssh telnet
## login local


### connecting to a network device using paramiko
### better to ping a device and linux server using ssh and paramiko
### test network connection betwen admin host and device that runs in GNS3
## test ssh using putty

## python object like putty

import paramiko
import time # this is to invoke the sleep function
import getpass

password = getpass.getpass('Enter password') # pycharm uses a modified console which is incompatible with getpass module, pycharm does not display
#since getpass has a differnet console... please run this python script from powershell module
#get pass module does not display the password whrn you are typing on screen
#Many programs that interact with the user via the terminal need to ask the user for password values
# without showing what the user types on the screen. The getpass module provides a portable way to handle such password prompts securely.
#$ python getpass_stream.py >/dev/null


ssh_client = paramiko.SSHClient()
print(type(ssh_client))

## call another method that autoamtically accepts the server host key
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh_client.connect(hostname='10.1.1.10', port='22',username='u1', password ='cisco', look_for_keys=False, allow_agent=False)
### not using ssh agent or keys , which is another application that keeps decrypted copy of private key in ram memory
### when ssh client authenticates an ssh server, it uses a finger print to identify it
### host key is randomly generated when ssh server is setup ssh-ed25519 and used to identify the server u r connected to
### ssh client implemented by paramiko cannot verify the servers host key , therefore this error

## check whether connection is active
print(ssh_client.get_transport().is_active())

### sending commands


print('Closing connection')
ssh_client.close()


### paramiko, better way to connect method of the SSHClinet() object
### python dictionary is also obtained from json file
## make sure the arguments match the name of the file i.e. hostname , port ,username and password are python arguments


#######keyword arguments **kwarg
router = {'hostname': '10.1.1.10', 'port':'22', 'username': 'u1', 'password': password } ## password is the variable password defined above
print(f'connecting to a {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False )

print(ssh_client.get_transport().is_active())


## securing the password of the router dictionary

###sending commands to cisco device

## create a shell object by invoking invoke_shell of the ssh client

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n') ## always add \n
shell.send('show version\n')
shell.send('show  ip interface brief\n')
time.sleep(1)  # from import time

output = shell.recv(10000)  ## this is output of the "show version command using shell.send"
print(type(output))  # type is bytes
output = output.decode('utf-8')   ## utf-8 is the default anyway
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()

# the advantage of using dictionary and argument unpacking is we can use those values in other parts of the script and they also stay connected



### configure OSPF on multiple routers

router1= {'hostname': '10.1.1.10','port':'22','username':'u1','password':'cisco'}
router2= {'hostname': '10.1.1.20','port':'22','username':'u1','password':'cisco'}
router3= {'hostname': '10.1.1.30','port':'22','username':'u1','password':'cisco'}

routerss = [router1,router2,router3]

for router in routerss:
    print(f'connecting to {routerss["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('cisco\n')  ### this is the enable password\
    shell.send('configure t\n')
    shell.send('router ospf 1\n')
    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('show ip protocols\n')
    time.sleep(2)

    output = shell.recv(10000).decode()  # decode is utf-8
    print(output)

    ### the above  configuration needs to be applied to multiple devices

####### putting outputs to another file

#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Set policy to use when connecting to servers without a known host key
#ssh.connect(hostname=host, username=user, password=secret, port=port)
#stdin, stdout, stderr = ssh.exec_command('sh ver')
#output = stdout.readlines()

#file = open('sh_ver.txt', 'w')
#file.write(''.join(output))
#file.close()