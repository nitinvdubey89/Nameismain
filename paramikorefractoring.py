#import paramiko
#import time
#import getpass


#ssh_client = paramiko.SSHClient()
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#router1= {'hostname': '10.1.1.10','port':'22','username':'u1','password':'cisco'}
#router2= {'hostname': '10.1.1.20','port':'22','username':'u1','password':'cisco'}
#router3= {'hostname': '10.1.1.30','port':'22','username':'u1','password':'cisco'}

#routerss = [router1,router2,router3]

#for router in routerss:
#    print(f'connecting to {routerss["hostname"]}')
#    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
#    shell = ssh_client.invoke_shell()
#    shell.send('enable\n')
#    shell.send('cisco\n')  ### this is the enable password\
#    shell.send('configure t\n')
#    shell.send('router ospf 1\n')
#    shell.send('net 0.0.0.0 0.0.0.0 area 0\n')
#    shell.send('end\n')
#    shell.send('terminal length 0\n')
#    shell.send('show ip protocols\n')
#    time.sleep(2)

#    output = shell.recv(10000).decode()  # decode is utf-8
#    print(output)


####### we are building a module that solves multiple problems i.e. decoding output, executing commands,
import paramiko
import time
import getpass


def connect(server_ip, server_port, user, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname = server_ip, port = server_port, username= user, password = passwd,
                       look_for_keys=False, allow_agent=False)
    return ssh_client # this we do so that the function can retrun a value so that a variable can use

def getsh(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n = 10000):  # it will simply return the output from shell's buffer
    output = shell.recv(n)
    return output.decode()

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing Connection')
        ssh_client.close()


if __name__ == '__main__': # the items mentioned below dont get executed by other modules
    router1= {'server_ip': '10.1.1.10','server_port':'22','user':'u1','passwd':'cisco'}
    router2= {'hostname': '10.1.1.20','port':'22','username':'u1','password':'cisco'}
    router3= {'hostname': '10.1.1.30','port':'22','username':'u1','password':'cisco'}

    routerss = [router1,router2,router3]


    client =  connect(**router1)
    shell = get_shell(client)

    send_command(shell,'enable')
    send_command(shell,'cisco')
    send_command(shell,'terminal length 0')
    send_command(shell, 'show version')
    send_command(shell,'show ip int brief')

    output = show(shell)
    print(output)