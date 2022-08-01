## shutil, os and subprocess
#a number of high level operations, copying, removing, renaming or deleiting
# some file operations can also be done using OS module
# many python programmers prefer to use shutil because it hides the complexity of operations
#shutil functions are built on top of OS module and each call may represent a lot of other calls to lower level files
# each directory contains a text file
# examplle two directories A and B
# each directory contains a text file
# there are more functions used to copy files in directories
# first function will take a look at is copy files i.e. src  ==> destination file
# source file and destination file are valid path names given as strings
# keep in minde , copy files functions copies only the content of the file,
# other metadata like the files' permissions, files creation and modification timmes are not preserved
#
import shutil
shutil.copyfile('C:\\Users\\Nitin\\Desktop\\GCP\\file a test\\Presentation1.pptx' , 'C:\\Users\\Nitin\\Desktop\\GCP\\file b test\\srx1.pptx') # if file already exisit then the file will be overwritten
## copy function , copies the data in file permissions mode, other metadata and file creation is not preserved
# insted of copy file, we use copy
shutil.copy('C:\\Users\\Nitin\\Desktop\\GCP\\file a test\\Presentation1.pptx' , 'C:\\Users\\Nitin\\Desktop\\GCP\\file b test\\srx2.pptx') # if file already exisit then the file will be overwritten
#copy will copy the file from one location to another  , name remains the same
#From a glance at the docs, it seems like you might want to use copyfile when you want
# to be sure the thing you are copying is a file and not a directory, whereas shutil.copy
# behaves more like the Unix command cp (working for both files and directories.)

#copy() also copies permission bits, as well as the contents of the file. copyfile only copies the data.

#Well Python implementation is interpreted,
# however python is compiled type too since once you run your python code it generates a .pyc file which is a compiled file
# but it's not for developers use as it is inaccessible.

#A compiled language is a programming language
# whose implementations are typically compilers and not interpreters.
# An interpreted language is a programming language whose implementations execute instructions directly and freely,
# without previously compiling a program into machine-language instructions

#In a compiled language, the target machine directly translates the program.
# In an interpreted language, the source code is not directly translated by the target machine.
# Instead, a different program, aka the interpreter, reads and executes the code.10 Jan 2020

# in order to preserve file metadata i.e file creation and modification times and permission
# take care even the hifh level function copyto cannot copy the permissions in metadata
#on windoews information like file owner or ACL are not copied

shutil.copy2('C:\\Users\\Nitin\\Desktop\\GCP\\file a test\\Presentation1.pptx' , 'C:\\Users\\Nitin\\Desktop\\GCP\\file a test\\ppppp.pptx') # if file already exisit then the file will be overwritten
## to recursively copy , use the copytree function. the destunation directory if does not exist will be created
# persimssions and times of directories are copied with copy start function and indivisual files are copied using copy2 function

shutil.copytree('C:\\Users\\Nitin\\Desktop\\GCP\\file a test' , 'C:\\Users\\Nitin\\Desktop\\GCP\\file c test') # if file already exisit then the file will be overwritten

#move function
# renaming
shutil.move('C:\\Users\\Nitin\\Desktop\\GCP\\file a test' , 'C:\\Users\\Nitin\\Desktop\\GCP\\a') # if file already exisit then the file will be overwritten

moving
shutil.move('C:\\Users\\Nitin\\Desktop\\GCP\\a' , 'C:\\Users\\Nitin\\Desktop\\GCP\\file c test')

#The cp command will copy your file(s) while the mv one will move them. So, the difference is that cp will keep the old file(s) while mv won't
#Between drives, 'mv' should essentially amount to cp + rm (copy to destination, then delete from source).
# On the same filesystem, 'mv' doesn't actually copy the data, it just remaps the inode, so it is far faster than cp.

#The inode (index node) is a data structure in a Unix-style file system that describes a file-system object such as a file or a directory.
# Each inode stores the attributes and disk block locations of the object's data.
#An inode is a data structure on a traditional Unix-style file system such as ext3 or ext4. storing the properties of a file and directories. Linux extended filesystems such as
# ext3 or ext4 maintain an array of these inodes called the inode table. This table contains list of all files in that filesystem
#An inode is an internal data structure that Linux uses to store information about a filesystem object.
# The inode count equals the total number of files and directories in a user account or on a disk. Each file or directory adds 1 to the inode count.


#delete the directory

shutil.rmtree('C:\\Users\\Nitin\\Desktop\\GCP\\a' , 'C:\\Users\\Nitin\\Desktop\\GCP\\file c test')


import os # works on window linux or mac

os.popen('arp -a')
# return is special file object that can be read

output = os.popen('arp -a').read()
output1= os.popen('ls -l /etc').read()
print(output)
print(output1)


# creating empy text file on desktop
os.system('type nul > c:\\Users\\ad\\Desktop\\abc.txt')
# 0 means no error





## SUBPROCESS MODULE#############
import subprocess
# subprocess module provides more powerful facilities for spawning new processes and retrieving their results
# using subprocess is preferrable to using OS module
# advantage is subprocess over system is that its more flexible i.e. we have access to stdout, stderr and standard inpt, real status code
#offers better error handling

#subprocess.check_call() and subprocess.check_output()

# check call runs the command with argument and waits for the comamnd to complete if the return code was 0 it means three was no error
# otherwise it raises call process exception error
# check_output to run  a command and capture its output
# the argument of  check_output  is a list that has as elements the command and its arguments

cmd = ['arp', '-a']
subprocess.check_output(cmd)
# returns an object of type bytes
# we can convert the byte object using the decode method
#
cmd = ['ping', '-n', '2', '8.8.8.8']
output = subprocess.check_output(cmd)
# this opens cmd
str_output = output.decode()
print(str_output)


## need to check pprint



# while making a program in python , we may need to execute some shell commands for our program.
# running external or shell command is very popular with python dev.
# os and subprocess modules are ideal example.
# lets see the first example on how to execute a command using the OS module
# p.open(), opens a pipe to or from command and return a value which is open file

#A pipe is a form of redirection (transfer of standard output to some other destination)
# that is used in Linux and other Unix-like operating systems to
# send the output of one command/program/process to another command/program/process for further processing.


#A pipe is a form of redirection (transfer of standard output to some other destination)
# that is used in Linux and other Unix-like operating systems to send the output of
# one command/program/process to another command/program/process for further processing.
# The Unix/Linux systems allow stdout of a command to be connected to stdin of another command.
# You can make it do so by using the pipe character ‘|’.


#Pipe is used to combine two or more commands, and in this,
# the output of one command acts as input to another command,
# and this command’s output may act as input to the next command and so on.
# It can also be visualized as a temporary connection between two or more commands/ programs/ processes.
# The command line programs that do the further processing are referred to as filters.


# syntax
#command_1 | command_2 | command_3 | .... | command_N

# ls -l -> temp
#more -> temp (or more temp)
#[contents of temp]
#rm temp


#example , ls -l | more
#The more command takes the output of $ ls -l as its input.
# The net effect of this command is that the output of ls -l is displayed one screen at a time.
# The pipe acts as a container which takes the output of ls -l and gives it to more as input.
# This command does not use a disk to connect standard output of ls -l to the standard input of more because pipe is implemented in the main memory.
#In terms of I/O redirection operators, the above command is equivalent to the following command sequence.


#$ ls -l -> temp
#more -> temp (or more temp)
#[contents of temp]
#rm temp


#2. Use sort and uniq command to sort a file and print unique values.

#$ sort record.txt | uniq
#$ cat sample2.txt | head -7 | tail -5
#This command select first 7 lines through (head -7) command and that will be input to (tail -5)
# command which will finally print last 5 lines from that 7 lines.

#3.4. Use ls and find to list and print all lines matching a particular pattern in matching files.

#$ ls -l | find ./ -type f -name "*.txt" -exec grep "program" {} \;


#4. 5. Use cat, grep, tee and wc command to read the particular entry from user and store in a file and print line count.

#$ cat result.txt | grep "Rajat Dua" | tee file2.txt | wc -l
#This command select Rajat Dua and store them in file2.txt and print total number of lines matching Rajat Dua
#Output :


#6. qmake is the default generator of Qt and has a very simple project file format.
# cmake is an advanced generator that has more complex input files but can also achieve things such as finding dependencies, etc
#make is typically used to build executable programs and libraries from source code. Generally speaking,
# make is applicable to any process that involves executing arbitrary commands to transform a source file to a target result


#Enum is a class in python for creating enumerations, which are a set of symbolic names (members) bound to unique, constant values.
# The members of an enumeration can be compared by these symbolic anmes, and the enumeration itself can be iterated over.