import paramikorefractoring
import getpass


username = input('Username:')
password = getpass.getpass() ## this should prompt for a password

#getpass.getpass(prompt='Password: ', stream=None)
#Prompt the user for a password without echoing.
# The user is prompted using the string prompt, which defaults to 'Password: '.
# On Unix, the prompt is written to the file-like object stream using the replace error handler if needed.
# stream defaults to the controlling terminal (/dev/tty) or if that is unavailable to sys.stderr
# (this argument is ignored on Windows)


#Linux refers to the kernel of the GNU/Linux operating system.
# More generally, it refers to the family of derived distributions.
# Unix refers to the original operating system developed by AT&T.

new_user = input('Enter the user you want to create')
command = 'sudo useradd -m -d /home/' + new_user + ' -s /bin/bash user2 ' + new_user # the space between ' s  is mandatory
ssh_client = paramikorefractoring.connect('192.168.0.13',2299, username, password)
remote_connection = paramikorefractoring.getsh(ssh_client)
paramikorefractoring.send_command(remote_connection,command)
paramikorefractoring.send_command(remote_connection,password)
print('A new user has been created ')

input('Display the users ? <y|n>')
if answer == 'y':
    users = paramikorefractoring.send_command(remote_connection, 'cat /etc/passwd')
    print(users.decode())

paramikorefractoring.close(ssh_client)

#sudo useradd username
#When executed without any option, useradd creates a new user account using the default settings specified in the /etc/default/useradd file.
#The command adds an entry to the /etc/passwd, /etc/shadow, /etc/group and /etc/gshadow files.
#To be able to log in as the newly created user, you need to set the user password. To do that run the passwd command followed by the username:
#sudo passwd username
#sudo useradd -m username
#Use the -m (--create-home) option to create the user home directory as /home/username:
#By default useradd creates the user’s home directory in /home.
# If you want to create the user’s home directory in other location, use the d (--home) option.
#sudo useradd -m -d /opt/username username
#In Linux and Unix-like operating systems, users are identified by unique UID and username.
#User identifier (UID) is a unique positive integer assigned by the Linux system to each user.
# The UID and other access control policies are used to determine the types of actions a user can perform on system resources.
#By default, when a new user is created, the system assigns the next available UID from the range of user IDs specified in the login.defs file.
#sudo useradd -u 1500 username
#id -u username ==> verify
#Creating a User with Specific Group ID #
#Linux groups are organization units that are used to organize and administer user accounts in Linux.
# The primary purpose of groups is to define a set of privileges such as reading, writing, or executing permission for a given resource that can be shared among the users within the group.
#When creating a new user, the default behavior of the useradd command is to create a group with the same name as the username, and same GID as UID.
#sudo useradd -g users username
#id -gn username  ==> verify group name
#Creating a User and Assign Multiple Groups #
#There are two types of groups in Linux operating systems Primary group and Secondary (or supplementary) group.
# Each user can belong to exactly one primary group and zero or more secondary groups.
#777 - all can read/write/execute (full access). 755 - owner can read/write/execute, group/others can read/execute. 644 - owner can read/write, group/others can read only.
#In Unix and Unix-like operating systems, chmod is the command and system call used to change the access permissions of file system objects sometimes known as modes. It is also used to change special mode flags such as setuid and setgid flags and a 'sticky' bit. The request is filtered by the umask. Wikipedia
#-rw-r--r-- 12 linuxize users 12.0K Apr  8 20:51 filename.txt
#|[-][-][-]-   [------] [---]
#| |  |  | |      |       |
#| |  |  | |      |       +-----------> 7. Group
#| |  |  | |      +-------------------> 6. Owner
#| |  |  | +--------------------------> 5. Alternate Access Method
#| |  |  +----------------------------> 4. Others Permissions
#| |  +-------------------------------> 3. Group Permissions
#| +----------------------------------> 2. Owner Permissions
#+------------------------------------> 1. File Type
#The first character shows the file type. It can be a regular file (-), directory (d), a symbolic link (l), or any other special type of file.
#The next nine characters represent the file permissions, three triplets of three characters each. The first triplet shows the owner permissions, the second one group permissions, and the last triplet shows everybody else permissions. The permissions can have a different meaning depending on the file type.
#In the example above (rw-r--r--) means that the file owner has read and write permissions (rw-), the group and others have only read permissions (r--).
#Each of the three permission triplets can be constructed of the following characters and have a different effects, depending on whether they are set to a file or to a directory:
#Effect of Permissions on Files
#ADVERTISING

#lshw
#-businfo
#Outputs
#the
#device
#list
#showing
#bus
#information, detailing
#SCSI, USB, IDE and PCI
#addresses.



#24.2.2 Termination Signals
#These signals are all used to tell a process to terminate, in one way or another. They have different names because they’re used for slightly different purposes, and programs might want to handle them differently.
#
#The reason for handling these signals is usually so your program can tidy up as appropriate before actually terminating. For example, you might want to save state information, delete temporary files, or restore the previous terminal modes. Such a handler should end by specifying the default action for the signal that happened and then reraising it; this will cause the program to terminate with that signal, as if it had not had a handler. (See Handlers That Terminate the Process.)

#The (obvious) default action for all of these signals is to cause the process to terminate.

#Macro: int SIGTERM
#The SIGTERM signal is a generic signal used to cause program termination. Unlike SIGKILL, this signal can be blocked, handled, and ignored. It is the normal way to politely ask a program to terminate.

#The shell command kill generates SIGTERM by default.

#Macro: int SIGINT
#The SIGINT (“program interrupt”) signal is sent when the user types the INTR character (normally C-c). See Special Characters, for information about terminal driver support for C-c.

#Macro: int SIGQUIT
#The SIGQUIT signal is similar to SIGINT, except that it’s controlled by a different key—the QUIT character, usually C-\—and produces a core dump when it terminates the process, just like a program error signal. You can think of this as a program error condition “detected” by the user.

#See Program Error Signals, for information about core dumps. See Special Characters, for information about terminal driver support.

#Certain kinds of cleanups are best omitted in handling SIGQUIT. For example, if the program creates temporary files, it should handle the other termination requests by deleting the temporary files. But it is better for SIGQUIT not to delete them, so that the user can examine them in conjunction with the core dump.

#Macro: int SIGKILL
#The SIGKILL signal is used to cause immediate program termination. It cannot be handled or ignored, and is therefore always fatal. It is also not possible to block this signal.

#This signal is usually generated only by explicit request. Since it cannot be handled, you should generate it only as a last resort, after first trying a less drastic method such as C-c or SIGTERM. If a process does not respond to any other termination signals, sending it a SIGKILL signal will almost always cause it to go away.

#In fact, if SIGKILL fails to terminate a process, that by itself constitutes an operating system bug which you should report.

#The system will generate SIGKILL for a process itself under some unusual conditions where the program cannot possibly continue to run (even to run a signal handler).

#Macro: int SIGHUP
#The SIGHUP (“hang-up”) signal is used to report that the user’s terminal is disconnected, perhaps because a network or telephone connection was broken. For more information about this, see Control Modes.

#This signal is also used to report the termination of the controlling process on a terminal to jobs associated with that session; this termination effectively disconnects all processes in the session from the controlling terminal. For more information, see Termination Internals.

