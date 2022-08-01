## creating class for telentlib to remove duplicate tasks
import time

class Device:
    def __init__(self ,host, username, password, tn= None):  ## constructor name is __init__
                self.host = host                                             # what are the attributes ,
                self.username = username                             # self is the referencee to the object that calls the methods
                self.password = password                             # name on the left side are object attributes and right side is methods arguments
                self.tn = tn

    def connect(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host)

    def authenticate(self):
        self.tn.read_until(b'Username:')
        self.tn.write(self.username.encode() + b'\n')  # we are doing enter with \n
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send(self,command, timeout=0.5):
        print(f'Sending command: {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def show(selfs):
        output = self.tn.read_all().decode('utf-8')
        return output

    def send_from_list(self, commands):
        for cmd in commands:
            self.send(cmd)

router1 = {'host': '10.1.1.10', 'user': 'u1', 'password': 'cisco', 'enable_password': 'cisco', 'loopback_ip': '1.1.1.1'}
router1 = {'host': '10.1.1.20', 'user': 'u1', 'password': 'cisco', 'enable_password': 'cisco', 'loopback_ip': '1.1.1.2'}
router1 = {'host': '10.1.1.30', 'user': 'u1', 'password': 'cisco', 'enable_password': 'cisco', 'loopback_ip': '1.1.1.3'}

routers = [router1,router2,router3]

router1 = Device(**routers)

# rather than sending router.send , we can define another method in the class i.e. send method, list of commands and uses a for loop to iterate over commands

commands = ['enable', 'cisco', 'config t', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'router ospf 1',
            'net 0.0.0.0 0.0.0.0 area 0', 'end', 'terminal length 0' , 'show ip protocols' , 'exit']

for r in routers:
    router = Device(host = r['host'], username= r['user'], password= r['password'])
    router.connect()
    router.authenticate()
    router.send_from_list(commands)

    #router.send('enable')
    #router.send(r['enable_password'])
    #router.send('config t')
    #router.send('interface loopback 0')
    #router.send(f'ip address {r["loopback_ip"]} 255.255.255.255')
    #router.send('exit')
    #router.send('router ospf 1')
    #router.send('net 0.0.0.0 0.0.0.0 area 0')
    #router.send('end')
    #router.send('terminal length 0')
    #router.send('show ip protocols')
    #router.send('exit')
    #output = router1.show()
    print(output)
    print('#'*50)


