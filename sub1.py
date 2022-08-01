import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    # this co-routine will return an instance  of the process class where process is a high level wrapper
    # that allows the communication with subprocesses and watches for their completion
    #proc =
    stdout , stderr =  await proc.communicate()
    # this returns the tuple with two elemets, stdout and stderr
    # this reads data from standard output and standard error untill EOF is reached and waits for the process to termminate
    # each linux command returns a status code which is 0 if there is no error  and different from 0  if there was an error
    # we get the status code by accessing the return code attribute of the proc object
    # print (f'(cmd) exited with status code: { proc.returncode}')
    print(f'{cmd} exited with status code: {proc.returncode}]')

    if stdout:
        print(f'STDOUT:\n {stdout.decode()}') # stdout is of type bytes and we are decoding to strings, default decode is utf-8

    if stderr:
        print(f'STDERR:\n {stderr.decode()}')

# top level co-routine

async def main(commads):
    tasks = []
    for cmd in commads:
        tasks.append(run(cmd))

    await asyncio.gather(*tasks)

commands = ('ipconfig' , 'arp -a')
asyncio.run(main(commands))
