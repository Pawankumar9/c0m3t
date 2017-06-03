# Python 3.5.2 or 3.6.1 or later is required!
import socket
import time
import os
import struct
import telnetlib

# Connect to target server
def connect(address, port):
    return socket.create_connection((address, port))

# Program Banner
print('Command Shell Stealer')
print('Exploitation')
