##PKA  on ciscoios and linux
#PKA is authentication method uses key-pair for authentication insted of a password
# this type is more secure, becasue password method suffers from security vulnerabilities like brute-force attack or keyloggers on the clinet
# other advantange is that we are able to login to server within script and automation tool that run unattended
# rsycn pr config management tool like ansible can run using a cron withoyt any human interverntion
#PKA has two type : public and private key
# public and private key transfer the copy of public key to the ssh server which the user wants to secure access
# private is kept locally and used to identify the userw when the user attempts to connect to the server
# anyone thaat has the public key will be able to encrypt data that can only be decrypted by the device that has the private key
# protecting private key is important therefore we should encrypt the private key with a passphrase
# client will be asked to provide the pasphrase or by entering the passphrase once and caching the key for later use

#The cache in Linux is called Page Cache.
#It is that certain amount of system memory that the kernel reserves for caching the file system disk accesses.
# This is to make overall performance faster. During Linux read system calls, the kernel checks if the cache contains the requested blocks of data
# open ssh contains a tool called ssh-agent that caches this memroy

#Linux maintains four caches of I/O data: page cache, i-node cache, buffer cache and directory cache.
#ssh-add ~/.ssh/id_rsa

#What is the difference between a DF command and a free command in UNIX?
#DF
#df - report file system disk space usage

#Description

#This manual page documents the GNU version of df.
# df displays the amount of disk space available on the file system containing each file name argument.
# If no file name is given, the space available on all currently mounted file systems is shown.
# Disk space is shown in 1K blocks by default, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used.

#If an argument is the absolute file name of a disk device node containing a mounted file system,
# df shows the space available on that file system rather than on the file system containing the device node.
# this version of df cannot show the space available on unmounted file systems because
# on most kinds of systems doing so requires very nonportable intimate knowledge of file system structures.

#‘Free’ command
#free - Display amount of free and used memory in the system

#Description

#Free displays the total amount of free and used physical and swap memory in the system,
# as well as the buffers and caches used by the kernel. The information is gathered by parsing /proc/meminfo. The displayed columns are:

#Total- Total installed memory (MemTotal and SwapTotal in /proc/meminfo)

#Used-Used memory (calculated as total - free - buffers - cache)

#free- Unused memory (MemFree and SwapFree in /proc/meminfo)

#shared- Memory used (mostly) by tmpfs (Shmem in /proc/meminfo)

#buffers- Memory used by kernel buffers (Buffers in /proc/meminfo)

#cache- Memory used by the page cache and slabs (Cached and SReclaimable in /proc/meminfo)



######ROUTER WILL BE SSH SERVER , ROUTER WILL BE SSH SERVER ########
### port 22 is closed on the router
### lets see if port 22 is open "telnet port 22"
## configure router
### hostname R1 # mandatory for ssh
## ip domain-name domain.com
## cryto key generate rsa  ## go for atleast 2048 bits, client will not authenticate to this server with such a short key
## ip ssh version 2 # now port 22 is open

## confgiure the vty lines to accept ssh connection and local c

##line vty 0 4
#### transport input ssh telnet
### login local


# copy windows public key to cisco router
# username windows_user
##key-string (paste the public key), it is possible to add multiple public  key to a single user for multiple devices to login

#'show running config | begin pubkey'

# cat /home/student/.ssh/id_rsa.pub # public is small
# cat /home/student/.ssh/id_rsa
# cisco ios only supports 2048 bits long, we can use the linux command fold to break the public key into multiple fragment
# use man fold
# wrap each input line to fit in a specified width
# fold -b -w 72 /home/student/.ssh/id_rsa.pub
# remove the ssh-rsa part and copy the key into a file

# ip ssh pubkey-chain
## username linux user
## key-string
## paste the key
## exit
#exit
#exit
#write
#show running config | begin pubkey

## ssh-keygen -l -f  -E md5 /home/student/.ssh/id_rsa.pub

# CONFIGURE the router to use authentication password
## no ip server authenticate user password
## no ip server authenticate user keyboard


#On Unix-like systems, including Linux, the system load is a measurement of the computational work the system is performing. This measurement is displayed as a number. A completely idle computer has a load average of 0. Each running process either using or waiting for CPU resources adds 1 to the load average. So, if your system has a load of 5, five processes are either using or waiting for the CPU.

#Unix systems traditionally just counted processes waiting for the CPU, but Linux also counts processes waiting for other resources — for example, processes waiting to read from or write to the disk.

#us: Amount of time the CPU spends executing processes for people in “user space.”
#sy: Amount of time spent running system “kernel space” processes.
#ni: Amount of time spent executing processes with a manually set nice value.
#id: Amount of CPU idle time.
#wa: Amount of time the CPU spends waiting for I/O to complete.
#hi: Amount of time spent servicing hardware interrupts.
#si: Amount of time spent servicing software interrupts.
#st: Amount of time lost due to running virtual machines (“steal time”).


#The column headings in the process list are as follows:

#PID: Process ID.
#USER: The owner of the process.
#PR: Process priority.
#NI: The nice value of the process.
#VIRT: Amount of virtual memory used by the process.
#RES: Amount of resident memory used by the process.
#SHR: Amount of shared memory used by the process.
#S: Status of the process. (See the list below for the values this field can take).
#%CPU: The share of CPU time used by the process since the last update.
#%MEM: The share of physical memory used.
#TIME+: Total CPU time used by the task in hundredths of a second.
#COMMAND: The command name or command line (name + options).


#The status of the process can be one of the following:

#D: Uninterruptible sleep
#R: Running
#S: Sleeping
#T: Traced (stopped)
#Z: Zombie


#Read-copy update (RCU) is a synchronization mechanism that was added to the Linux kernel in October of 2002.
# RCU achieves scalability improvements by allowing reads to occur concurrently with updates.
# In contrast with conventional locking primitives that ensure mutual exclusion among concurrent threads regardless of
# whether they be readers or updaters, or with reader-writer locks that allow concurrent
# reads but not in the presence of updates, RCU supports concurrency between a single updater and multiple readers.
# RCU ensures that reads are coherent by maintaining multiple versions of objects and ensuring
# that they are not freed up until all pre-existing read-side critical sections complete.
# RCU defines and uses efficient and scalable mechanisms for publishing and reading new versions of an object,
# and also for deferring the collection of old versions.
# These mechanisms distribute the work among read and update paths in such a way as to make read paths extremely fast.
# In some cases (non-preemptable kernels), RCU's read-side primitives have zero overhead.

#RCU is made up of three fundamental mechanisms, the first being used for insertion,
# the second being used for deletion, and the third being used to allow readers to tolerate concurrent insertions and deletions.
# These mechanisms are described in the following sections, which focus on applying RCU to linked lists:








































