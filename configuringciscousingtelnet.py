#telnet is simple and security is not an issue
#compared to ssh , telnet is not secure, connection is not encrypted but in clear text
# another protocol can secure the telnet, using VPN or SITE OR PRIVATE LAN
# only if there is another layer of security applied, use SSH
import getpass
import telnetlib # python standard library , it provides a telnet class
import time


## below variable set is for single device
host = '10.1.1.10'
port ='23'
user = 'u1'
password = 'cisco'

## create dictionary for each device

router1 = {'host': '10.1.1.10', 'user': 'u1', 'password': 'cisco'}
router2 = {'host': '10.1.1.20', 'user': 'u1', 'password': 'cisco'}
router3 = {'host': '10.1.1.30', 'user': 'u1', 'password': 'cisco'}

routers = [router1,router2,router3]

for router in routers:
    print(f'Connecting to {router["host"]}') ## its allowed to use double quotes inside single quotes
    password = getpass.getpass('Enter password')


    tn = telnetlib.Telnet(host=router['host'])

    # to pause the script when its asking for username , we will call readuntil method

    tn.read_until(b'Username:')
    tn.write(router['user'].encode() + b'\n')  # we are doing enter with \n
    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    # telnetlib only works wit bytes
    tn.write(b'terminal length 0')
    # tn.write(b'show ip interface brief \n') # the command below with encode does the same thing
    tn.write(b'show ip interface brief \n'.encode())
    tn.write(password.encode() + b'\n')
    # pycharm uses a modified console which is incompatible with getpass module therefore it hangs
    # you have to run the script in a terminal
    # run the script from powershell or cmd

    tn.write(b'cisco\n')  # this is the enable password
    tn.write(b'config t\n')
    tn.write(b'ip route  0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
    tn.write(b'end\n')
    tn.write(b'show ip route\n')
    tn.write(b'exit\n')
    time.sleep(1)  # dont forget to add this line

    output = tn.read_all()  # reading all data from connections buffer
    print(type(output))
    output = output.decode()
    print(output)
    print('#'*50)

# create a telnet object by calling telnetlib method of telnet class which is a constructor

tn = telnetlib.Telnet(host = host , port = port)

# to pause the script when its asking for username , we will call readuntil method

tn.read_until(b'Username:')
tn.write(user.encode() + b'\n')  # we are doing enter with \n
tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

# telnetlib only works wit bytes
tn.write(b'terminal length 0')
#tn.write(b'show ip interface brief \n') # the command below with encode does the same thing
tn.write(b'show ip interface brief \n'.encode())
tn.write(b'enable\n')
tn.write(b'cisco\n') # this is the enable password
tn.write(b'show run\n')
tn.write(b'exit\n')
time.sleep(1) # dont forget to add this line

output  = tn.read_all() # reading all data from connections buffer
print(type(output))
output = output.decode()
print(output)