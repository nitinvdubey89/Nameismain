# demsg
# dmesg is used to examine or control the kernel ring buffer. The default action is to display all messages from the kernel ring buffer.
#dmesg is a command on most Unix-like operating systems that prints the message buffer of the kernel. The output includes messages produced by the device drivers
#In computing, tty is a command in Unix and Unix-like operating systems to print the file name of the terminal connected to standard input. tty stands for TeleTYpewrite
#The /dev/ directory consists of files that represent devices that are attached to the local system

#In order to test the pyserial module and automate the configuration of networking devices over serial connections, you need a physical device to connect to.

#However, there is a way to simulate a serial console in GNS3 and connect to it from a Linux machine (tested with Ubuntu, GNS3 is installed and runs on Ubuntu).
import sys
import pyserial # its a module for serial connection
import time


import serial

def open_console(port='com3', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8):
    console =  serial.Serial(port='com3', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False

def run_command(console, cmd='\n', sleep=1):
    print('Sending command:' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)

def read_from_console(console):
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        return output.decode()
    else:
        print('nOTHING TO BE READ FROM SERIAL CONNECTION')
        return False

def check_initial_configuration_dialog(console): #
    run_command(console, '\n')
    prompt  = read_from_console(console) ## reading from console messages
    if 'Would you like to enter the intial configuration dialog?' in prompt:
        run_command(console,'no' , 15)
        run_command(console, '\r\n') #==> \r\n is used by some OS like older windows or older MACOS runs better with some cisco devices
        return True
    else:
        return False


con = open_console()
run_command(con)
run_command(con,'show version')
output = read_from_console()
print(output)

################################# below is function based code

with serial.Serial(port='/dev/tty/USBO', baudrate = 9600, parity = 'N', stopbits = 1, bytesize = 8, timeout = 8) as console:#with statement will autmoatically close t
    if console.isOpen():
        print('Serial is Opened')
    else:
        sys.exit()

    with serial.Serial(port='com3', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8) as console: # with statement will autmoatically close the connection
        if console.isOpen():
            print('Console successfully opened!')
            console.write(b'\n')
            time.sleep(1)
            console.write(b'enable\n')
            time.sleep(1)
            console.write(b'terminal length 0\n')
            time.sleep(1)
            console.write(b'show version\n')
            time.sleep(3)
            bytes_to_be_read  = console.inWaiting()
            output = console.read(bytes_to_be_read)
            print(output.decode())
        else:
            print('Error opening the console connection')
            sys.exit()

            bytesToBeRead = console.inWaiting()

        # write into a serial connection

    ## read from a serial connections i.e bytes in read mode

        bytesToBeRead  = console.inWaiting()

    # number of bytes to be read from console
        consoleData = console.read(bytesToBeRead)
        print(consoleData.decode())
    console.write(b'\n')
    time.sleep(1)  ## this is mandatory

