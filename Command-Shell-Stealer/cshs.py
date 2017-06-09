# Python 3.5.2 or 3.6.1 or later is required!
import sys
import socket
import time
import os
import struct
import telnetlib

omSymbol = '[*]' # Output message symbol
imSymbol = '[+]' # Input message symbol
ipSymbol = '[>]' # Input prompt symbol
wmSymbol = '[!]' # Warning message symbol
emSymbol = '[-]' # Error message symbol

# Applying the color to the symbols if the operating system is Linux
if os.name == 'posix':
    omSymbol = '\x1b[1;34m' + omSymbol + '\x1b[1;0m' # Blue
    imSymbol = '\x1b[1;32m' + imSymbol + '\x1b[1;0m' # Green
    ipSymbol = '\x1b[1;36m' + ipSymbol + '\x1b[1;0m' # Cyan
    wmSymbol = '\x1b[1;33m' + wmSymbol + '\x1b[1;0m' # Yellow
    emSymbol = '\x1b[1;31m' + emSymbol + '\x1b[1;0m' # Red

# Target server connection
def connect(address, port):
    return socket.create_connection((address, port))

# Packing data from x86 platform
def x86pack(data):
    return struct.pack('<I', data)

# Unpacking data from x86 platform
def x86unpack(data):
    return struct.unpack('<I', data)[0]

# Packing data from x64 platform
def x64pack(data):
    return struct.pack('<Q', data)

# Unpacking data from x64 platform
def x64unpack(data):
    return struct.unpack('<Q', data)[0]

# Interactive mode on telnet
def interact(targetServer):
    print(omSymbol + ' Interactive mode')
    telnetConnection = telnetlib.Telnet()
    telnetConnection.sock = targetServer
    telnetConnection.interact()

# Program banner
print('Command Shell Stealer Nu')
print('Exploitation')

# Target server address and port input
try:
    targetServerAddress = sys.argv[1]
    print(omSymbol + ' Target server address is ' + targetServerAddress + '.')
except IndexError:
    print(imSymbol + ' Input target server address.')
    targetServerAddress = input(ipSymbol + ' ')

try:
    targetServerPort = sys.argv[2]
    print(omSymbol + ' Target server port is ' + targetServerPort + '.')
except IndexError:
    print(imSymbol + ' Input target server port.')
    targetServerPort = input(ipSymbol + ' ')

# Warning message for chargen service
if targetServerPort == '19':
    print(wmSymbol + ' Chargen is too dangerous for buffered writer!')
    print(imSymbol + ' Do you want to continue it? [yes/no]')
    answerCode = ''
    while answerCode != 'yes':
        answerCode = input(ipSymbol + ' ')
        if answerCode == 'yes':
            print(omSymbol + ' You chose to connect to chargen.')
        elif answerCode == 'no':
            print(omSymbol + ' Exiting Command Shell Stealer...')
            exit()
        else:
            print(emSymbol + ' Incorrect answer entered.')
    print(omSymbol + ' Preparing to connect to chargen...')

# TODO: Write payload input code here!

# Connecting to target server
targetServer = connect(targetServerAddress, targetServerPort)

# TODO: Write exploit code here!

# Running interactive mode
interact(targetServer)
