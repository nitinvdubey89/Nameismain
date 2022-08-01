## scp
import paramiko
from scp import SCPClinet
import time

## first we connect to the device using paramiko
ip_address = '10.0.0.1'
username = andrei
password = 'cisco'

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname= ipaddress, port=22,username = u1,password =cisco, allow_agent = False, look_for_keys = False)

scp = SCPClinet(ssh_client.get_transport())
#get_transport()
#Return The underlying Transport object for this SSH connection. This can be used to perform lower-level tasks, like opening specific kinds of channels.
#Returns: The Transport for this connection

## copy a single file
scp.put('devices.txt', '/tmp/aa.txt')

### if we dont use /tmp then the aa.txt will be copied to /home/andrei directoru
### if aa.txt already existing then this will overwrite the config


## copy a directory from this machine to linux server

scp.put('directory1', recursive=True , remote_path='/tmp')

## getting a file from a remote location
scp.get('/etc/passwd', 'passwd')

## window path will have back slash
scp.get('/etc/passwd', 'C:\\Users\\ad\\passwd-from-linux.txt')

## we should have permissions also

#load_system_host_keys(filename=None)
#Load host keys from a system (read-only) file. Host keys read with this method will not be saved back by save_host_keys.
#This method can be called multiple times. Each new set of host keys will be merged with the existing set (new replacing old if there are conflicts).
#If filename is left as None, an attempt will be made to read keys from the user’s local “known hosts” file, as used by OpenSSH, and no exception will be raised if the file can’t be read. This is probably only useful on posix.

scp.close()


#ssh remote cat file1 file2 ... > locale-file
#scp remote:{file1,file2...} local-dir


#$ mkfifo p
#$ while :; do cat p >> output ; done  &
#$ scp somehost:test/\* p
#bar       100%    4    10.9KB/s   00:00
#doo       100%    4     8.6KB/s   00:00
#foo       100%    4    13.6KB/s   00:00
#$ kill %1
## output contains the files concatenated

#rsync -avzh username@remoteserverip:/remoteserverpath/Mergedfile localserverpath_where_you_want_to_save
