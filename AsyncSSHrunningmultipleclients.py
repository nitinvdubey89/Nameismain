import asyncio
import asyncssh

async def run_client(host, username, password, commands):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
       return await connection.run(command)
# host is the ipaddress of remote ssh deamon

async def run_mulitple_clients(hosts):
    tasks = []
    for host in hosts:
        tasks = run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(tasks)

    results = await asyncio.gather(*tasks, return_exceptions=True)

    i = 0
    for result in results:
        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')
#The isinstance() function returns True if the specified object is of the specified type, otherwise False.

#If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
#x = isinstance("Hello", (float, int, str, list, dict, tuple))


        elif result.exit_status != 0:
            print(f'Task {i} exited with status {result.exit_status}:')
            print(result.stderr, end='')
        else:  # and the else branch for the case where was neither an Exception was raised nor an error occurred.
            print(f'Task {i} succeeded:')
            print(result.stdout, end='')
        print('#'* 50 )


hosts = [
    {'host':'192.168.0.50', 'username': 'student', 'password': 'student' , 'command': 'ifconfig'},
    {'host':'192.168.0.50', 'username': 'student', 'password': 'student' , 'command': 'ifconfig'},
    {'host':'192.168.0.50', 'username': 'student', 'password': 'student' , 'command': 'who -a '},
    {'host':'192.168.0.50', 'username': 'student', 'password': 'student' , 'command': 'uname -a '},
]

asyncio.run(run_mulitple_clients(hosts))

#hostOS# cat /sys/module/kvm_intel/parameters/nested == Y 