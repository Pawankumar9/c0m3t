# Python 3.5.2 or 3.6.1 or later is required!
import socket
import time
import os
import struct
import telnetlib

# Target server connection
def connect(address, port):
    return socket.create_connection((address, port))

# Packing on x86 platform
def x86pack(data):
    return struct.pack('<I', data)

# Unpacking on x86 platform
def x86unpack(data):
    return struct.unpack('<I', data)[0]

# Packing on x64 platform
def x64pack(data):
    return struct.pack('<Q', data)

# Unpacking on x64 platform
def x64unpack(data):
    return struct.unpack('<Q', data)

# Program Banner
print('Command Shell Stealer')
print('Exploitation')
