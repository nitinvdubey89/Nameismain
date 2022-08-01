import paramiko
import getpass
import time

ssh_clinet = paramiko.SSHClient()

ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
linux = {'hostname': '192.168.0.50', 'port': '22', 'username': 'u1', 'password': 'pass123'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('sudo cat /etc/shadow\n')
shell.send('pass123\n')
time.sleep(1)

output = shell.recv(10000).decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)
#def execute_command(self, command, out_streams = [sys.stdout], err_streams = [sys.stderr], poll_intervals = POLL_INTERVALS):
#I read a bit online, and found out that happens because there's no actual terminal behind the ssh session.
#But then I found out that I'm losing the ability to get data to stderr on the channel
#  (everything goes to stdout for some reason, i.e. channel.recv_stderr_ready() is never True). Indeed, I found in the doc the following:

stdin.write('pass123\n')
time.sleep(2)

## to check whether the command was executed succesfully  we can add verfication

stdin, stdout, stderr =  ssh_clinet.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())
time.sleep(1)


output1  = stdout.read().decode()
print(output1)