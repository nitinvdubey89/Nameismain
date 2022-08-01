## check on the linux VM about the ip address
## ssh the vm and it should work
## t

## sudo systemctl status ssh
# Systemctl is a systemd utility that is responsible for Controlling
# the systemd system and service manager.
# Systemd is a collection of system management daemons,
# utilities, and libraries which serves as a replacement of System V init daemon.29 Apr 2015

import paramiko
import time
import getpass
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.0.50', 'port': '22', 'username': 'u1', 'password': 'pass123'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('/etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')
shell.send('pass123\n')
time.sleep(1)

### another method of sending commands to linux server and have its own standard input/output and error exec_command method

output = shell.recv(10000).decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n')
output1  = stdout.read().decode()
print(output1)

stdin, stdout, stderr = ssh_client.exec_command('whoasad\n')### stderr test, execute a non existent command
time.sleep(0.5)  ### we are waiting for a small period of time to complete execution and write to output buffer
output1  = stdout.read().decode()
print(output1)
print(stderr.read().decode()) # here we can see the error the bash error will show command not found


stdin, stdout, stderr = ssh_client.exec_command('cat /etc/shadow\n')### stderr test, execute a non existent command
time.sleep(0.5)  ### we are waiting for a small period of time to complete execution and write to output buffer
output1  = stdout.read().decode()
print(output1)
print(stderr.read().decode()) #here we will recieve permission denied


### stdout.read() is bytes therefore we need the decode function

## exec comamnd will return a tuple with 3 elements of type paramiko channel , channel file i.e. stdin, stdout,err
if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()