# Python 3.5.2 or 3.6.1 or later is required!
import sys
import socket
import time
import os
import struct
import telnetlib

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
    print('* Interactive mode')
    telnetConnection = telnetlib.Telnet()
    telnetConnection.sock = targetServer
    telnetConnection.interact()

# Program banner
print('Command Shell Stealer')
print('Exploitation')

# Target server address and port input
try:
    targetServerAddress = sys.argv[1]
    print('* Target server address is '+targetServerAddress)
except IndexError:
    print('@ Input target server address')
    targetServerAddress = input('> ')

try:
    targetServerPort = sys.argv[2]
    print('* Target server port is '+targetServerPort)
except IndexError:
    print('@ Input target server port')
    targetServerPort = input('> ')

# Connecting to target server
targetServer = connect(targetServerAddress, targetServerPort)

# TODO: Write code here!

# Running interactive mode
interact(targetServer)
