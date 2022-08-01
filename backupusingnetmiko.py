from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

start = time.time()

def back(device): ### this is the target functon i.e. the function executed by each thread
    connection = ConnectHandler(**cisco_device)  ## **kwargs way
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_command('show run')
    # print(output)
    prompt = connection.find_prompt()
    hostname = prompt[
               0:-1]  ## starting from 0th element to the last element bnbut the last element will be excluded , this is called slicing
    # example s= python s[0:-1] = 'pytho' , s[0:-2]  = 'pyth'
    print(hostname)

    now = datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    # file_name = f'{router1["server-ip"]}_{year}--{month}-{day}.txt'
    # print(file_name)

    filename = f'{hostname}_{year}-{month}-{day}_backup.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'backup of {hostname} completed successfully')
        print('#' * 30)

    print('closing connection ')
    connection.disconnect()


with open('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()
for ip in devices:
    device = {
                  device_type:'cisco_ios',
                  host : ip ,
                  username: 'u1',
                  password: 'cisco',
                  port:'22',
                  secret: 'cisco' ,
                  verbose: True
                }
    #backup(device)
    th = threading.Thread(target=backup , args=(device,))  ## args is a tuple
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()


## this method is really slow ; concurrent execution is implemented using multi-processing or multi-threading
## script is very slow
##one thread per device
# first we create a list that stores the thread
#



end = time.time()

print(f'total execution time {end-start}')