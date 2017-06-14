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

# Program options
optionProgramManual = '-h'
optionTargetType = '-t'
codeTargetTypeLocal = ':local'
codeTargetTypeRemote = ':remote'

# Program manual
def manual():
    if os.name == 'nt':
        print(omSymbol + ' Usage on Windows')
        print(' python cshs.py [option] [<address> <port>]\n')
    elif os.name == 'posix':
        print(omSymbol + ' Usage on Linux')
        print(' python3 cshs.py [option] [<address> <port>]\n')
    else:
        print(emSymbol + ' Usage on ' + os.name + ' is not exist!')
        exit()
    print(omSymbol + ' Options list')
    print(' ' + optionProgramManual + '\t'*3 + 'Print this manual.')
    print(' ' + optionTargetType + ':<local | remote>\tStart this program.')
    exit()

# Target server connection creation
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

# Variables initialization
answerCode = ''
optionCode = ''
targetType = ''
targetServerAddress = ''
targetServerPort = ''

# Option code decoder
try:
    if sys.argv[1] == optionProgramManual:
        manual()
    elif sys.argv[1].startswith(optionTargetType) == True:
        print(omSymbol + ' Starting Command Shell Stealer...')
        optionCode = sys.argv[1]
        targetType = optionCode.replace(optionTargetType, '')
    else:
        print(emSymbol + ' Invalid option entered!')
        print(omSymbol + ' Type \"-h\" option if you need some help.')
        exit()
except IndexError:
    print(emSymbol + ' No option has been entered.')
    print(omSymbol + ' Starting Command Shell Stealer...')
    print(imSymbol + ' Input target type. [:local/:remote]')
    targetType = input(ipSymbol + ' ')

# Target server address and port input
# FIXME: Put all of these codes into If ~ Else!
try:
    targetServerAddress = sys.argv[2]
    print(omSymbol + ' Target server address is ' + targetServerAddress + '.')
except IndexError:
    print(imSymbol + ' Input target server address.')
    targetServerAddress = input(ipSymbol + ' ')

try:
    targetServerPort = sys.argv[3]
    print(omSymbol + ' Target server port is ' + targetServerPort + '.')
except IndexError:
    print(imSymbol + ' Input target server port.')
    targetServerPort = input(ipSymbol + ' ')

if targetServerPort.isdigit() == False:
    print(emSymbol + ' Invalid target server port entered!')
    exit()

# Warning message for chargen service
if targetServerPort == '19':
    print(wmSymbol + ' Chargen is too dangerous for buffered writer!')
    print(imSymbol + ' Do you want to continue it? [yes/no]')
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
    answerCode = ''

# TODO: Write payload input code here!

# Connecting to target server
targetServer = connect(targetServerAddress, targetServerPort)

# TODO: Write exploit code here!

# Running interactive mode
interact(targetServer)
