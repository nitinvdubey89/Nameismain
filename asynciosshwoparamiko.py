#paramiko does not support async.io
# paramiko is great for ssh but
# paramiko does not support async.io but only threading , which is not good for scaling
#concurrency and network IO
# async ssh is a python
# library which provides an
# async clinet and server implemetnation  of SSHV2 protocol on top of async.io
# full support for sshv2, sftp and scp clinet and server function and allows multiple sumultabneous connection over a single SSH connection

import asyncssh
import asyncio

async def connect_and_run(host, username, password, commands):
   async with asyncssh.connect(host= host ,username = username, password = password, known_hosts = None  ) as connection:
       #result = await connection.run(command)
       #return result

       ## to run a command on the remote device , i will call the run method of  the connection object.
       # host is the method argument in the left side and the host on the right side is my functions argument

      # 2. run multiplle commands
      results = []
      for cmd in commands:
          result = await connection.run(cmd)
          results.append(result)
      return results

commands = ('ifconfig','who -a', 'uname -a')
result= asyncio.run(connect_and_run('192.168.0.50', 'lab', 'lab123', commands))
for result in results:
    print(f'STDOUT:\n {result.stdout}')
    print(f'STDERR:\n {result.stderr}')
    print('#'*50)
## result variable is not of type string , it has more components like standard output and standard error
#print(f'STDOUT:\n {result.stdout}')
#print(f'STDERR:\n {result.stderr}')